from django.test import TestCase
from core.models import Hotel, Room, Reservation
from users.models import Person, CustomUser
from datetime import date

class HotelModelTest(TestCase):
    def test_str_method(self):
        hotel = Hotel.objects.create(name="Grand Hotel", city="NYC", address="123 Main St", stars=5)
        self.assertEqual(str(hotel), "Grand Hotel - (5 Stars)")

class RoomModelTest(TestCase):
    def test_str_method(self):
        hotel = Hotel.objects.create(name="Grand Hotel", city="NYC", address="123 Main St", stars=4)
        room = Room.objects.create(hotel=hotel, number="101", capacity=2, price_per_night=150.00)
        self.assertEqual(str(room), "Room 101 in Grand Hotel")

class ReservationModelTest(TestCase):
    def test_str_method(self):
        user = CustomUser.objects.create(username="john_doe")
        person = Person.objects.create(user=user, birth_date="1990-01-01")
        hotel = Hotel.objects.create(name="Grand Hotel", city="NYC", address="123 Main St", stars=4)
        room = Room.objects.create(hotel=hotel, number="101", capacity=2, price_per_night=150.00)
        reservation = Reservation.objects.create(
            person=person, hotel=hotel, room=room, start_at=date(2025, 2, 1), end_at=date(2025, 2, 5)
        )
        self.assertEqual(
            str(reservation),
            "john_doe at Grand Hotel (2025-02-01 to 2025-02-05)"
        )
