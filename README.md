# Hotel Reservation System
This project is a simple hotel reservation system built with Django REST Framework. It provides functionality for managing hotels, rooms, and reservations. Users can create accounts and book reservations while ensuring proper validation and data integrity.

## Table of Contents:
- [Features](https://github.com/shadishahab/hotel-booking#features)
- [Technologies Used](https://github.com/shadishahab/hotel-booking#technologies-used)
- [API Endpoints](https://github.com/shadishahab/hotel-booking#api-endpoints)
- [Installation and Running](https://github.com/shadishahab/hotel-booking#installation)
- [Testing](https://github.com/shadishahab/hotel-booking#testing)


## Features
- **JWT Authentication** using `djangorestframework-simplejwt`.
- **Reservation System**: Create reservations with validation for overlapping or duplicate bookings.
- **Date Validation**: Prevent reservations with invalid dates (end date before the start date or dates in the past).
- **Atomic Transactions**: Ensure data consistency using Django’s transaction.atomic for preventing race condition.
- **Unit and integration tests**.
- **Swagger** auto-documentation.


## Technologies Used
- Python 3.13
- Django 5.1
- Django REST Framework 3.15
- PostgreSQL as the database.
- JWT for authentication (`djangorestframework-simplejwt`: 5.3)
- `drf-yasg` for building swagger documentation.
- `python-decouplle` for managing environment variables.


# API Endpoints

## Reservation Endpoint
- **POST** `/core/reservation/create/`: Create a reservation by providing hotel, start date, and end date.
Request example:
```json
{
    "hotel": 1,
    "start_at": "2025-02-01",
    "end_at": "2025-02-05"
}
```

Response example (success):
```json
{
    "id": 1,
    "hotel": 1,
    "room": 2,
    "start_at": "2025-02-01",
    "end_at": "2025-02-05"
}
```

### How it works

The user sends the checkin and checkout dates, along with their desired hotel in.
Then, the `get_available_room` function iterates through that hotel's rooms to find a room with no reservation on the requested period.
If successful, a new `Reservation` object is created and if not, user gets the error message `No rooms are available for the selected dates.`

**Notes**:
1. The process of finding an available room is done via calling the function `get_available_room` in `utils.py` because of the Single-Responsibility Principle. (So the view is solely for creating a new `Reservation` object.)
2. The `Reservation` model is both related to `Hotel` and `Room`. But since the `room` field is automatically assigned, there would be no data inconsistency.
3. I had previously implemented a simpler, more efficient logic in `get_available_room` which utilized django ORM querying, but it failed in some cases. The previous logic can still be seen in `utils.py` as commented lines.


## Auth Endpoints
- **POST** `/api/token/`: Obtain a JWT token.
- **POST** `/api/token/refresh/`: Refresh a JWT token.


## Installation
Follow these steps to set up the project locally:

1. Clone the Repository
```bash
git clone https://github.com/shadishahab/hotel-booking.git
cd booking
```
2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install Dependencies
```bash
  pip install -r requirements.txt
```
4. Set Up the Database
Create a PostgreSQL database
Update the `DATABASES` settings in `settings.py` with your database credentials.
5. Apply Migrations
```bash
python manage.py migrate
```
6. Create a Superuser
```bash
python manage.py createsuperuser
```
7. Run the Development Server
```bash
python manage.py runserver
```
(The project requires some environment variables. Create a `.env` file in the root directory with your database credentials and secret key)

**Note**: `DEBUG` has been left `True` for your testing purposes.

## Testing
Run the following command to execute all tests:
```bash
python manage.py test
```

To run a specific test file (e.g., test_views.py in the core app):
```bash
python manage.py test core.tests.test_views
```
