from django.contrib import admin
from .models import Hotel, Room, Reservation

class HotelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city','address', 'stars', 'phone_number']
    list_display_links = ['id', 'name']
    list_filter = ['city', 'stars']


class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'hotel', 'number','capacity', 'price_per_night']
    list_display_links = ['id', 'number']
    list_filter = ['hotel', 'capacity']


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'person', 'hotel','room', 'start_at', 'end_at', 'status', 'created_at', 'updated_at']
    list_filter = ['person', 'hotel', 'room']


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Hotel, HotelAdmin)