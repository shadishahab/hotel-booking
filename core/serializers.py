from django.utils.timezone import now
from rest_framework import serializers
from .models import Reservation, Hotel

class ReservationRequestSerializer(serializers.Serializer):
    hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all())
    start_at = serializers.DateField()
    end_at = serializers.DateField()

    def validate(self, data):
        if data['start_at'] < now().date() or data['end_at'] < now().date():
            raise serializers.ValidationError("Start and end dates must not be in the past.")
        if data['start_at'] > data['end_at']:
            raise serializers.ValidationError("End date must be after or equal to the start date.")
        return data
    

class ReservationResponseSerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(source="hotel.id", read_only=True)

    class Meta:
        model = Reservation
        fields = ['id', 'hotel', 'room', 'start_at', 'end_at']
