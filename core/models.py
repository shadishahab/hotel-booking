from django.db import models
from django.conf import settings


class Hotel(models.Model):
    pass


class Room(models.Model):

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
