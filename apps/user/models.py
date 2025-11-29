from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.common.models import BaseModel


class CustomUser(AbstractUser, BaseModel):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('CUSTOMER', 'Customer'),
    )
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CUSTOMER')
