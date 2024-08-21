from loguru import logger
from typing import Union

from models import Booking
from database.helper import process_sql, get_object, get_all_objects


def create_booking(booking: Booking) -> bool:
    SQL = f"""
        INSERT INTO bookings (seat_number, type, status, start, end, date, user_id)
        VALUES(
            '{booking.seat_number}',
            '{booking.type}',
            '{booking.status}',
            '{booking.start}',
            '{booking.end}',
            '{booking.date}',
            '{booking.user_id}'
        );
    """
    result = process_sql(SQL=SQL)
    if result:
        logger.success(
            f"Added booking for {booking.type} №{booking.seat_number} | start: {booking.start}, end: {booking.end}")
    else:
        logger.error(
            f"Error creating booking for {booking.type} №{booking.seat_number} | start: {booking.start}, end: {booking.end}")
    return result


def get_bookings() -> Union[list[Booking], None]:
    SQL = """
        SELECT * FROM bookings;
    """
    result = get_all_objects(SQL=SQL, table=Booking)
    return result


def get_bookings_by_tg_id(tg_id: str) -> Union[list[Booking], None]:
    SQL = f"""
        SELECT * FROM bookings
        WHERE user_id = '{tg_id}';
    """
    result = get_all_objects(SQL=SQL, table=Booking)
    return result
