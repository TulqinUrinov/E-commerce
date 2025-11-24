from typing import TYPE_CHECKING

from django.db import models
from django.db.models import SET_NULL

from data.common.models import BaseModel

if TYPE_CHECKING:
    from data.file.models import File


class Product(BaseModel):
    name = models.CharField(max_length=100)
    image: "File" = models.ForeignKey("file.File", on_delete=SET_NULL, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name
