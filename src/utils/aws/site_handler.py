"""AWS site gneeration utilities."""
# Standard Python Libraries
from datetime import datetime
import json
import logging
import os
import time

# Third-Party Libraries
import boto3
from api.documents.active_site import ActiveSite


logger = logging.getLogger(__name__)

HOSTED_ZONE_ID = os.environ.get("HOSTED_ZONE_ID")
CONTENT_SOURCE = os.environ.get("SOURCE_BUCKET")
REGION = boto3.session.Session().region_name

# Initialize aws clients
acm = boto3.client("acm")
cloudfront = boto3.client("cloudfront")
s3 = boto3.client("s3")
s3_resource = boto3.resource("s3")
route53 = boto3.client("route53")


def launch_site(website, domain):
    """Launch an active site onto s3."""
    # get domain name
    domain_name = domain.get("Name")

    # setup s3 bucket
    setup_s3_bucket(bucket_name=domain_name, content_name=website.get("name"))

    # generate ssl certs and return certificate ARN
    certificate_arn = generate_ssl_certs(domain=domain)

    # setup cloudfront
    distribution_id, distribution_endpoint = setup_cloudfront(
        domain_name=domain_name, certificate_arn=certificate_arn
    )

    # Setup DNS
    setup_dns(domain=domain, endpoint=distribution_endpoint)

    return {
        "cloudfront": {
            "id": distribution_id,
            "distribution_endpoint": distribution_endpoint,
        },
        "acm": {"certificate_arn": certificate_arn},
    }


def delete_site(domain):
    """Delete an active site off s3."""
    domain_name = domain.get("Name")

    distributions = cloudfront.list_distributions()["DistributionList"]

    # TODO: Return distribution ID
    [distribution for distribution in distributions]

    # delete cloudfront distribution
    distribution_endpoint = cloudfront.delete_distribution(Id="")

    bucket = s3_resource.Bucket(domain_name)

    # delete all objects in bucket
    bucket.objects.all().delete()

    # set waiter
    waiter = s3.get_waiter("object_not_exists")
    waiter.wait(Bucket=domain_name, Key="index.html")

    # delete bucket
    s3.delete_bucket(Bucket=domain_name)

    response = delete_dns(domain=domain, endpoint=distribution_endpoint)
    return response


def setup_s3_bucket(bucket_name, content_name):
    """Setup a static website S3 Bucket."""
    available_buckets = [
        bucket.get("Name") for bucket in s3.list_buckets().get("Buckets")
    ]

    # create S3 bucket
    if bucket_name not in available_buckets:
        s3.create_bucket(Bucket=bucket_name)

    # set waiter
    waiter = s3.get_waiter("bucket_exists")
    waiter.wait(Bucket=bucket_name)

    # copy contents from source
    source_bucket = s3_resource.Bucket(CONTENT_SOURCE)
    source_keys = [
        obj.key for obj in source_bucket.objects.all() if content_name in obj.key
    ]

    for key in source_keys:
        copy_source = {
            "Bucket": CONTENT_SOURCE,
            "Key": key,
        }
        bucket = s3_resource.Bucket(bucket_name)
        bucket.copy(copy_source, key.replace(f"{content_name}/", ""))

    # attach bucket policy
    bucket_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AddPerm",
                "Effect": "Allow",
                "Principal": "*",
                "Action": ["s3:GetObject"],
                "Resource": "arn:aws:s3:::%s/*" % bucket_name,
            }
        ],
    }

    bucket_policy = json.dumps(bucket_policy)
    s3.put_bucket_policy(
        Bucket=bucket_name,
        Policy=bucket_policy,
    )

    # set waiter
    waiter = s3.get_waiter("object_exists")
    waiter.wait(Bucket=bucket_name, Key="index.html")

    # launch static site
    s3.put_bucket_website(
        Bucket=bucket_name,
        WebsiteConfiguration={"IndexDocument": {"Suffix": "index.html"}},
    )


def setup_cloudfront(domain_name, certificate_arn):
    """Setup AWS CloudFront Distribution."""
    # Launch CloudFront distribution
    unique_identifier = datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")

    distribution_config = {
        "CallerReference": unique_identifier,
        "Aliases": {
            "Quantity": 1,
            "Items": [domain_name],
        },
        "DefaultRootObject": "index.html",
        "Comment": "Managed by Domain Manager",
        "Enabled": True,
        "Origins": {
            "Quantity": 1,
            "Items": [
                {
                    "Id": "1",
                    "DomainName": f"{domain_name}.s3-website-{REGION}.amazonaws.com",
                    "CustomOriginConfig": {
                        "HTTPPort": 80,
                        "HTTPSPort": 443,
                        "OriginProtocolPolicy": "http-only",
                    },
                }
            ],
        },
        "DefaultCacheBehavior": {
            "TargetOriginId": "1",
            "ViewerProtocolPolicy": "redirect-to-https",
            "TrustedSigners": {
                "Quantity": 0,
                "Enabled": False,
            },
            "ForwardedValues": {
                "QueryString": False,
                "Cookies": {"Forward": "all"},
                "Headers": {
                    "Quantity": 0,
                },
                "QueryStringCacheKeys": {
                    "Quantity": 0,
                },
            },
            "MinTTL": 1000,
        },
        "ViewerCertificate": {
            "ACMCertificateArn": certificate_arn,
            "SSLSupportMethod": "sni-only",
            "MinimumProtocolVersion": "TLSv1.2_2019",
        },
    }

    distribution = cloudfront.create_distribution(
        DistributionConfig=distribution_config
    )

    return (
        distribution["Distribution"]["Id"],
        distribution["Distribution"]["DomainName"],
    )


def setup_dns(domain, endpoint=None, ip_address=None):
    """Setup a domain's DNS."""
    domain_name = domain.get("Name")
    dns_id = domain.get("Id")
    if ip_address:
        response = route53.change_resource_record_sets(
            HostedZoneId=dns_id,
            ChangeBatch={
                "Comment": ip_address,
                "Changes": [
                    {
                        "Action": "UPSERT",
                        "ResourceRecordSet": {
                            "Name": domain_name,
                            "Type": "A",
                            "TTL": 15,
                            "ResourceRecords": [{"Value": ip_address}],
                        },
                    }
                ],
            },
        )
    else:
        response = route53.change_resource_record_sets(
            HostedZoneId=dns_id,
            ChangeBatch={
                "Comment": domain_name,
                "Changes": [
                    {
                        "Action": "UPSERT",
                        "ResourceRecordSet": {
                            "Name": domain_name,
                            "Type": "A",
                            "AliasTarget": {
                                "HostedZoneId": "Z2FDTNDATAQYW2",
                                "EvaluateTargetHealth": False,
                                "DNSName": endpoint,
                            },
                        },
                    }
                ],
            },
        )
    logger.info(response)
    return response


def delete_dns(domain, endpoint=None, ip_address=None):
    """Setup a domain's DNS."""
    domain_name = domain.get("Name")
    dns_id = domain.get("Id")
    if ip_address:
        response = route53.change_resource_record_sets(
            HostedZoneId=dns_id,
            ChangeBatch={
                "Comment": ip_address,
                "Changes": [
                    {
                        "Action": "DELETE",
                        "ResourceRecordSet": {
                            "Name": domain_name,
                            "Type": "A",
                            "TTL": 15,
                            "ResourceRecords": [{"Value": ip_address}],
                        },
                    }
                ],
            },
        )
    else:
        response = route53.change_resource_record_sets(
            HostedZoneId=dns_id,
            ChangeBatch={
                "Comment": domain_name,
                "Changes": [
                    {
                        "Action": "DELETE",
                        "ResourceRecordSet": {
                            "Name": domain_name,
                            "Type": "A",
                            "AliasTarget": {
                                "HostedZoneId": "Z2FDTNDATAQYW2",
                                "EvaluateTargetHealth": False,
                                "DNSName": endpoint,
                            },
                        },
                    }
                ],
            },
        )
    logger.info(response)
    return response


def generate_ssl_certs(domain):
    """Request and Validate an SSL certificate using AWS Certificate Manager."""
    domain_name = domain.get("Name")
    dns_id = domain.get("Id")
    requested_certificate = acm.request_certificate(
        DomainName=domain_name,
        ValidationMethod="DNS",
        SubjectAlternativeNames=[
            domain_name,
        ],
        DomainValidationOptions=[
            {
                "DomainName": domain_name,
                "ValidationDomain": domain_name,
            },
        ],
        Options={"CertificateTransparencyLoggingPreference": "ENABLED"},
    )

    certificate_arn = requested_certificate["CertificateArn"]
    resource_records = {}
    while not resource_records:
        time.sleep(2)
        certificate_description = acm.describe_certificate(
            CertificateArn=certificate_arn
        )
        resource_records = [
            description.get("ResourceRecord", None)
            for description in certificate_description.get("Certificate", {}).get(
                "DomainValidationOptions"
            )
        ][0]

    # add validation record to the dns
    route53.change_resource_record_sets(
        HostedZoneId=dns_id,
        ChangeBatch={
            "Comment": domain_name,
            "Changes": [
                {
                    "Action": "UPSERT",
                    "ResourceRecordSet": {
                        "Name": resource_records["Name"],
                        "Type": "CNAME",
                        "TTL": 30,
                        "ResourceRecords": [
                            {
                                "Value": resource_records["Value"],
                            },
                        ],
                    },
                }
            ],
        },
    )

    # wait until the certificate has been validated
    waiter = acm.get_waiter("certificate_validated")
    waiter.wait(CertificateArn=certificate_arn)

    return certificate_arn
