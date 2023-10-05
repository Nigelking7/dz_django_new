from django.db import models
from django.contrib.auth.models import AbstractUser


class ApiUser(AbstractUser):
    choice_type = [
        ('P', 'provider'),
        ('C', 'consumer')
    ]

    choice = models.CharField(max_length=1, choices=choice_type)


class Storage(models.Model):
    name = models.CharField(max_length=120)
    goods = models.JSONField(default=dict)


class Good(models.Model):
    name = models.CharField(max_length=120)



