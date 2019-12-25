from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    type = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.username