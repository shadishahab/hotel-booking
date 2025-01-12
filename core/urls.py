from django.urls import path
from .views import ReservationCreateAPIView

urlpatterns = [
    path('reservation/create/', ReservationCreateAPIView.as_view(), name='reservation-create'),
]