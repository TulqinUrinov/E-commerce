import uuid

from django.db import models


class BaseModel(models.Model):
    """
    Base model that provides a UUID primary key and automatic timestamp fields.

    Fields:
        id (UUIDField): Primary key using a universally unique identifier (UUID)
            instead of the default auto-incrementing integer. This ensures global
            uniqueness and avoids ID collisions across distributed systems.

        created_at (DateTimeField): Timestamp automatically set when the object
            is created. Useful for tracking when a record was first added.

        updated_at (DateTimeField): Timestamp automatically updated every time
            the object is saved. Helps track the latest modification time.

    This model is intended to be inherited by other models in the project to
    maintain consistent ID and timestamp behavior across the application.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
