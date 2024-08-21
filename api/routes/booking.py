from fastapi import APIRouter

from database import create_booking, get_bookings, get_bookings_by_tg_id
from models import Booking

router = APIRouter(prefix="/booking", tags=["booking"])


@router.post("/add")
async def createBooking(booking: Booking):
    result = create_booking(booking=booking)

    return result

@router.get("/all")
async def getBookings():
    bookings = get_bookings()

    return [booking.to_dict() for booking in bookings] if bookings else None


@router.get("/{tg_id}")
async def getBookingsByTgId(tg_id: str):
    bookings = get_bookings_by_tg_id(tg_id=tg_id)

    return [booking.to_dict() for booking in bookings] if bookings else None
