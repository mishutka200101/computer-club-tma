from dataclasses import dataclass, asdict
from typing import Literal


@dataclass
class Booking:
    seat_number: int
    type: Literal["PS", "PC"]
    status: Literal["ACTIVE", "CANCELED"]
    start: str
    end: str
    date: str
    user_id: str
    id: int = None

    def to_dict(self):
        return asdict(self)
