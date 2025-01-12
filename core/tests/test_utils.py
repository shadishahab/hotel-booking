from django.test import TestCase
from core.models import Hotel, Room, Reservation
from core.utils import get_available_room
from datetime import date
from users.models import Person, CustomUser

class GetAvailableRoomTest(TestCase):
    def setUp(self):
        self.hotel = Hotel.objects.create(name="Grand Hotel", city="NYC", address="123 Main St", stars=5)
        self.room1 = Room.objects.create(hotel=self.hotel, number="101", capacity=2, price_per_night=150.00)
        
        self.user = CustomUser.objects.create(username="john_doe")
        self.person = Person.objects.create(user=self.user, birth_date="1990-01-01")

    def test_available_room(self):
        room = get_available_room(self.hotel, date(2025, 2, 1), date(2025, 2, 5))
        self.assertEqual(room, self.room1)

    def test_no_available_room(self):
        Reservation.objects.create(
            person=self.person, hotel=self.hotel, room=self.room1, start_at=date(2025, 2, 1), end_at=date(2025, 2, 5)
        )
        with self.assertRaises(ValueError) as context:
            get_available_room(self.hotel, date(2025, 2, 1), date(2025, 2, 5))
        self.assertEqual(str(context.exception), "No rooms are available for the selected dates.")
