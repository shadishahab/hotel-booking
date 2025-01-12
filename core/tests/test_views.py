from rest_framework.test import APITestCase
from rest_framework import status
from core.models import Hotel, Room, Reservation
from users.models import CustomUser, Person
from datetime import date

class ReservationCreateAPITest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="test_user", password="password123")
        self.person = Person.objects.create(user=self.user, birth_date="1990-01-01")

        self.hotel = Hotel.objects.create(name="Grand Hotel", city="NYC", address="123 Main St", stars=5)
        self.room1 = Room.objects.create(hotel=self.hotel, number="101", capacity=2, price_per_night=150.00)

        self.client.login(username="test_user", password="password123")

    def test_create_reservation_success(self):
        response = self.client.post('/core/reservation/create/', {
            "hotel": self.hotel.id,
            "start_at": "2025-02-01",
            "end_at": "2025-02-05"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)
        self.assertIn("room", response.data)

    def test_create_reservation_no_rooms_available(self):
        Reservation.objects.create(
            person=self.person, hotel=self.hotel, room=self.room1, start_at=date(2025, 2, 1), end_at=date(2025, 2, 5)
        )
        response = self.client.post('/core/reservation/create/', {
            "hotel": self.hotel.id,
            "start_at": "2025-02-01",
            "end_at": "2025-02-05"
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)

    def test_create_reservation_invalid_dates(self):
        response = self.client.post('/core/reservation/create/', {
            "hotel": self.hotel.id,
            "start_at": "2025-02-05",
            "end_at": "2025-02-01"
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("non_field_errors", response.data)
        self.assertIn("End date must be after or equal to the start date.", str(response.data['non_field_errors']))