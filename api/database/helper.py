import sqlite3
from typing import Union

from database.config import DATABASE
from models import PS
from models import User
from models import Booking


def process_sql(SQL: str) -> bool:
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute(SQL)
            conn.commit()
        return True
    except Exception:
        return False


def get_object(SQL: str, table: Union[PS, User, Booking]) -> Union[PS, User, Booking, None]:
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute(SQL)
            result = cursor.fetchone()
            if result:
                return table(*result)
        return None
    except Exception:
        return None


def get_all_objects(SQL: str, table: Union[PS, User, Booking]) -> Union[list[PS], list[User], list[Booking], None]:
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute(SQL)
            result = cursor.fetchall()
            result = [table(*res) for res in result]
        return result
    except Exception:
        return None
