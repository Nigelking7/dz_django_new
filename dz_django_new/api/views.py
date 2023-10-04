from django.db import models
from django.contrib.auth.models import AbstractUser


class ApiUser(AbstractUser):
    ...


class Hotel(models.Model):
    name = models.CharField(max_length=120)


class Room(models.Model):
    num = models.PositiveIntegerField()
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)


class Booking(models.Model):
    room = models.ForeignKey(Room, related_name='booking', on_delete=models.CASCADE)
    user = models.ForeignKey(ApiUser, related_name='bookings', on_delete=models.CASCADE)

