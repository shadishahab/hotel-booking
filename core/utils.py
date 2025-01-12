from .models import Reservation, Room

# def get_available_room(hotel, start_at, end_at):
#     """
#     Returns the first available room in the given hotel for the specified date range.
#     Raises a ValueError if no rooms are available.
#     """
#     available_room = Room.objects.filter(hotel=hotel).exclude(
#     Q(reservation__start_at__lt=end_at) & Q(reservation__end_at__gt=start_at)
# ).select_for_update().first()
#     if not available_room:
#         raise ValueError("No rooms available for the given dates.")
#     return available_room

def get_available_room(hotel, start_at, end_at):
    """
    Returns the first available room in the given hotel for the specified date range.
    Raises a ValueError if no rooms are available.
    """
    rooms = Room.objects.filter(hotel=hotel).select_for_update()
    for room in rooms:
        reservations = Reservation.objects.filter(room=room)
        for reservation in reservations:
            if (reservation.start_at<end_at) and (reservation.end_at>start_at):
                break
            if (reservation.start_at == start_at) and (reservation.end_at == end_at):
                break
        else:
            return room
    raise ValueError("No rooms are available for the selected dates.")
