from django.contrib.auth.models import User
from django.db import models


class login(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


# Create your models here.
