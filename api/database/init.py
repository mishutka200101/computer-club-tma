import sqlite3

from database.SQLs import PS_TABLE, USER_TABLE, BOOKING_TABLE
from database.config import DATABASE

TABLES = [
    USER_TABLE,
    PS_TABLE,
    BOOKING_TABLE
]


def init() -> None:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()

        for TABLE in TABLES:
            cursor.execute(TABLE)

        conn.commit()
