from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime

StatusType = Literal["ACTIVE", "DONE", "CANCELLED"]
SeatType = Literal["PC", "PS"]


class BookingModel(BaseModel):
    id: int
    seat_number: int
    seat_type: SeatType
    status: StatusType = "ACTIVE"
    start_date: datetime | str
    end_date: datetime | str
    created_at: Optional[datetime | str] = datetime.now()
    created_by: str
