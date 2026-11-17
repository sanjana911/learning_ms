from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    ROLE_CHOICES = (
        ("faculty", "Faculty"),
        ("student", "Student")
    )

    role = models.CharField(max_length=100, choices=ROLE_CHOICES)

    phone = models.CharField(max_length=15, unique=True)