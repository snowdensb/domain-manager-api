"""DNS Record Handler."""
# Third-Party Libraries
import boto3
import botocore

# cisagov Libraries
from utils.aws.regional_s3_endpoints import (
    REGIONAL_HOSTED_ZONE_ID,
    REGIONAL_WEBSITE_ENDPOINT,
)

route53 = boto3.client("route53")
s3 = boto3.client("s3")


def manage_record(action, hosted_zone_id, record):
    """Create record."""
    if record["record_type"] == "REDIRECT":
        return modify_redirect_record(action, hosted_zone_id, record)
    else:
        return modify_record(
            action,
            hosted_zone_id,
            record["name"],
            record["record_type"],
            record["config"]["value"],
            record["ttl"],
        )


def modify_record(
    action, hosted_zone_id, record_name, record_type, record_value, record_ttl
):
    """Modify a simple record in route53."""
    records = []
    for value in record_value.splitlines():
        records.append({"Value": value})

    try:
        resp = route53.change_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            ChangeBatch={
                "Changes": [
                    {
                        "Action": action,
                        "ResourceRecordSet": {
                            "Name": record_name,
                            "Type": record_type,
                            "TTL": record_ttl,
                            "ResourceRecords": records,
                        },
                    }
                ]
            },
        )
        return resp
    except botocore.exceptions.ClientError as error:
        if (
            error.response["Error"]["Code"] == "InvalidChangeBatch"
            and action == "DELETE"
        ):
            return None
        else:
            raise error


def modify_redirect_record(action, hosted_zone_id, record):
    """Modify records for redirects."""
    resp = route53.change_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        ChangeBatch={
            "Changes": [
                {
                    "Action": action,
                    "ResourceRecordSet": {
                        "Name": record["name"],
                        "Type": "A",
                        "AliasTarget": {
                            "DNSName": REGIONAL_WEBSITE_ENDPOINT,
                            "EvaluateTargetHealth": False,
                            "HostedZoneId": REGIONAL_HOSTED_ZONE_ID,
                        },
                    },
                }
            ]
        },
    )

    if action == "CREATE":
        s3.create_bucket(ACL="private", Bucket=record["name"])

        # modify bucket
        s3.put_bucket_website(
            Bucket=record["name"],
            WebsiteConfiguration={
                "RedirectAllRequestsTo": {
                    "HostName": record["config"]["value"],
                    "Protocol": record["config"]["protocol"],
                }
            },
        )

    if action == "DELETE":
        s3.delete_bucket(Bucket=record["name"])

    if action == "UPSERT":
        s3.put_bucket_website(
            Bucket=record["name"],
            WebsiteConfiguration={
                "RedirectAllRequestsTo": {
                    "HostName": record["config"]["value"],
                    "Protocol": record["config"]["protocol"],
                }
            },
        )

    return resp
