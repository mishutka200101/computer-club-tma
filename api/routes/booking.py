from fastapi import APIRouter

from database.crud import create_booking, get_bookings, get_active_bookings, get_user_bookings, get_bookings_by_seat, get_active_bookings_by_seat, edit_booking
from database.models.pydantic import BookingModel

router = APIRouter(prefix="/booking", tags=["booking"])


@router.get("/all")
async def getBookings() -> list[BookingModel] | None:
    bookings = get_bookings()

    return [booking.__data__ for booking in bookings] if bookings else None


@router.get("/user_bookings/{tg_id}")
async def getBookingsByTgId(tg_id: str) -> list[BookingModel] | None:
    bookings = get_user_bookings(tg_id=tg_id)

    return [booking.__data__ for booking in bookings] if bookings else None


@router.get("/active_bookings/")
async def getActiveBookings() -> list[BookingModel] | None:
    bookings = get_active_bookings()

    return [booking.__data__ for booking in bookings] if bookings else None


@router.post("/add")
async def createBooking(booking: BookingModel) -> bool:
    result = create_booking(booking=booking)

    return result
