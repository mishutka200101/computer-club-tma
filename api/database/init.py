from database import database
from database.models import (
    User,
    Booking,
    PS
)

MODELS = [
    User,
    Booking,
    PS
]


def init_db():
    with database.atomic():
        database.create_tables(MODELS)
