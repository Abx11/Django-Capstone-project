# user_auth/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username
