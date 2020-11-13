"""Application documents."""
# Standard Python Libraries
from datetime import datetime
from typing import Union

# Third-Party Libraries
from utils.db import Document


class Application(Document):
    """Application document model."""

    name: Union[str, None] = None
    requester_name: Union[str, None] = None
    created: Union[datetime, None] = None

    def __init__(self, _id=None):
        """Initialize collection name."""
        self._id = _id
        self.collection = "applications"

    def create(self, name):
        """Create a new application."""
        # make names unique if it does not already exist
        self.get_collection().create_index("name", unique=True)

        self.name = name
        self.requester_name = "Dev User"
        self.created = datetime.now()
        return super().create()
