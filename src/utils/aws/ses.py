"""Create DNS email records from SES."""
# cisagov Libraries
from utils.aws.clients import SES, Route53

route53 = Route53()
ses = SES()


def manage_resource_records(
    domain_name: str,
    action: str,
    verification_token: str,
):
    """Manage Route53 Records."""
    if f"{domain_name}." not in route53.list_hosted_zones(names_only=True):
        return "Domain's hosted zone does not exist."

    dns_id = "".join(
        hosted_zone.get("Id")
        for hosted_zone in route53.list_hosted_zones()
        if hosted_zone.get("Name") == f"{domain_name}."
    )

    return route53.client.change_resource_record_sets(
        HostedZoneId=dns_id,
        ChangeBatch={
            "Comment": "",
            "Changes": [
                {
                    "Action": action,
                    "ResourceRecordSet": {
                        "Name": f"_amazonses.{domain_name}",
                        "Type": "TXT",
                        "TTL": 300,
                        "ResourceRecords": [{"Value": f'"{verification_token}"'}],
                    },
                },
                {
                    "Action": action,
                    "ResourceRecordSet": {
                        "Name": domain_name,
                        "Type": "MX",
                        "TTL": 300,
                        "ResourceRecords": [
                            {"Value": "10 inbound-smtp.us-east-1.amazonaws.com"}
                        ],
                    },
                },
            ],
        },
    )


def enable_email_receiving(domain_name: str):
    """Enable receiving emails for a specified domain."""
    # Generate verification token
    verification_token = ses.verify_domain_identity_token(domain_name=domain_name)

    response = manage_resource_records(
        domain_name=domain_name,
        action="UPSERT",
        verification_token=verification_token,
    )

    return response


def disable_email_receiving(domain_name: str):
    """Disable receiving emails for a specified domain."""
    verification_token = ses.client.get_identity_verification_attributes(
        Identities=[domain_name]
    )["VerificationAttributes"][domain_name]["VerificationToken"]

    manage_resource_records(
        domain_name=domain_name,
        action="DELETE",
        verification_token=verification_token,
    )

    return ses.client.delete_identity(Identity=domain_name)
