from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('host', 'Host'),
        ('guest', 'Guest'),
    ]

    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='guest')

    def __str__(self):
        return self.username