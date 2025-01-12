from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db import transaction
from .models import Reservation
from .serializers import ReservationRequestSerializer, ReservationResponseSerializer
from .utils import get_available_room

class ReservationCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_serializer(self):
            return ReservationRequestSerializer()
    
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer = ReservationRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        hotel = data['hotel']
        start_at = data['start_at']
        end_at = data['end_at']

        try:
            available_room = get_available_room(hotel, start_at, end_at)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        reservation = Reservation.objects.create(
            person=request.user.person,
            hotel=hotel,
            room=available_room,
            start_at=start_at,
            end_at=end_at
        )

        response_serializer = ReservationResponseSerializer(reservation)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
