from database import database
from database.models import Booking
from database.models.pydantic import BookingModel
from database.utils.decorators import handle_errors


@handle_errors
def create_booking(booking_data: BookingModel):
    with database.atomic():
        booking = Booking.create(**booking_data.model_dump())
        return booking


@handle_errors
def get_bookings():
    with database.atomic():
        bookings = Booking.select()
        return bookings


@handle_errors
def get_active_bookings():
    with database.atomic():
        bookings = Booking.select().where(Booking.status == "ACTIVE")
        return bookings


@handle_errors
def get_user_bookings(tg_id: str):
    with database.atomic():
        bookings = Booking.select().where(Booking.created_by == tg_id)
        return bookings


@handle_errors
def get_bookings_by_seat(seat_number: int, seat_type: str):
    with database.atomic():
        bookings = Booking.select().where(Booking.seat_number == seat_number,
                                          Booking.seat_type == seat_type)
        return bookings


@handle_errors
def get_active_bookings_by_seat(seat_number: int, seat_type: str):
    with database.atomic():
        bookings = Booking.select().where(Booking.seat_number == seat_number,
                                          Booking.seat_type == seat_type,
                                          Booking.status == "ACTIVE")
        return bookings


@handle_errors
def edit_booking(booking_data: BookingModel):
    with database.atomic():
        res = Booking.update(**booking_data.model_dump()
                             ).where(Booking.id == booking_data.id).execute()
        return res
