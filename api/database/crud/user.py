from database import database
from database.models import User
from database.models.pydantic import UserModel
from database.utils.decorators import handle_errors


@handle_errors
def create_user(user_data: UserModel):
    with database.atomic():
        user = User.create(**user_data.model_dump())
        return user


@handle_errors
def get_or_create_user(user_data: UserModel):
    with database.atomic():
        user = User.get_or_create(**user_data.model_dump())
        return user


@handle_errors
def get_user(tg_id: str):
    with database.atomic():
        user = User.get_or_none(User.tg_id == tg_id)
        return user


@handle_errors
def get_all_users():
    with database.atomic():
        users = User.select()
        return users


@handle_errors
def edit_user(user_data: UserModel) -> bool | None:
    with database.atomic():
        user = User.get(User.tg_id == user_data.tg_id)
        for key, value in user_data.model_dump().items():
            setattr(user, key, value)
        user.save()
        return True
