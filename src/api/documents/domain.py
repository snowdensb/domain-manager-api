"""Domain documents."""
# Third-Party Libraries
from bson.objectid import ObjectId
from utils.db import Document, db


class Domain(Document):
    """
    Document model for domains.

    Note: DO NOT MODIFY. Domain data is managed by the route53.
    """

    def __init__(self, **kwargs):
        """Initialize arguments."""
        self.fields = [
            "Id",
            "Name",
            "CallerReference",
            "Config",
            "ResourceRecordSetCount",
            "Tags",
        ]
        self.document = {k: kwargs.get(k) for k in self.fields}

    @staticmethod
    def get_by_id(domain_id):
        """Get domain by id."""
        return db.domains.find_one({"_id": ObjectId(domain_id)})

    @staticmethod
    def get_all():
        """Get all registered domains."""
        return [x for x in db.domains.find()]

    @staticmethod
    def add_tag(domain_id, tag_id):
        """Add a tag to a domain document."""
        db.domains.find_one_and_update(
            {"_id": ObjectId(domain_id)}, {"$push": {"Tags": tag_id}}
        )