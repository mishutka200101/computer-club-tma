from loguru import logger
from typing import Union

from models import User
from database.helper import process_sql, get_object, get_all_objects


def create_user(user: User) -> bool:
    tg_id = user.tg_id
    username = user.username

    if not username:
        return False

    SQL = """
        INSERT INTO users (tg_id, username) VALUES('%s', '%s');
    """ % (tg_id, username)
    result = process_sql(SQL=SQL)
    if result:
        logger.success(f"Added User: {tg_id} / {username}")
    else:
        logger.error(f"Error adding User: {tg_id} / {username}")
    return result


def get_or_create_user(tg_id: str) -> User:
    SQL = f"""
        SELECT * FROM users
        WHERE tg_id='{tg_id}';
    """
    user = get_object(SQL=SQL, table=User)
    if not user:
        user = User(tg_id=tg_id)
        create_user(user=user)
    return user


def get_user(tg_id: str) -> Union[User, None]:
    SQL = f"""
        SELECT * FROM users
        WHERE tg_id='{tg_id}';
    """
    user = get_object(SQL=SQL, table=User)
    return user


def get_all_users() -> Union[list[User], None]:
    SQL = """
        SELECT * FROM users;
    """
    users = get_all_objects(SQL=SQL, table=User)
    return users
