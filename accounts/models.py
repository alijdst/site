from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True)
    phone_number = models.CharField(max_length=16, null=True)
