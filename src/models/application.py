"""Application document."""
# Standard Python Libraries
from datetime import datetime

# Third-Party Libraries
from utils.db.base import Document
from utils.db.datatypes import Stringtype, Datetime


class Application(Document):
    """Application document model."""

    name: Stringtype
    requester_name: Stringtype
    created: Datetime

    def __init__(self, _id=None):
        """Initialize collection and indices."""
        self._id = _id
        self.collection = "applications"
        self.indexes = ["name"]

    def create(self, name):
        """Create a new application."""
        self.name = name
        self.requester_name = "Dev User"
        self.created = datetime.now()
        return super().create()
