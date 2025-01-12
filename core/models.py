from django.db import models
from users.models import Person

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    address = models.TextField()
    stars = models.PositiveSmallIntegerField(choices=[(i, f'{i} Star') for i in range(1, 6)])
    phone_number = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - ({self.stars} Stars)"


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
    number = models.CharField(max_length=50)
    capacity = models.PositiveSmallIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('hotel', 'number')

    def __str__(self):
        return f"Room {self.number} in {self.hotel.name}"


class Reservation(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="reservations")
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="reservations")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="reservations")
    start_at = models.DateField()
    end_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('room', 'start_at', 'end_at')

    def __str__(self):
        return f"{self.person.user.username} at {self.hotel.name} ({self.start_at} to {self.end_at})"
