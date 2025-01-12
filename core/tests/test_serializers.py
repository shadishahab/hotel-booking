from django.test import TestCase
from core.models import Hotel
from core.serializers import ReservationRequestSerializer
from datetime import timedelta
from django.utils.timezone import now

class ReservationRequestSerializerTest(TestCase):
    def test_valid_data(self):
        hotel = Hotel.objects.create(name="Grand Hotel", city="NYC", address="123 Main St", stars=5)
        data = {
            "hotel": hotel.id,
            "start_at": "2025-02-01",
            "end_at": "2025-02-05"
        }
        serializer = ReservationRequestSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_dates_past(self):
        hotel = Hotel.objects.create(name="Grand Hotel", city="NYC", address="123 Main St", stars=5)
        data = {
            "hotel": hotel.id,
            "start_at": str(now().date() - timedelta(days=1)),
            "end_at": str(now().date() - timedelta(days=1))
        }
        serializer = ReservationRequestSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("Start and end dates must not be in the past.", str(serializer.errors))

    def test_invalid_date_range(self):
        hotel = Hotel.objects.create(name="Grand Hotel", city="NYC", address="123 Main St", stars=5)
        data = {
            "hotel": hotel.id,
            "start_at": "2025-02-05",
            "end_at": "2025-02-01"
        }
        serializer = ReservationRequestSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("End date must be after or equal to the start date.", str(serializer.errors))
