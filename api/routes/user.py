from fastapi import APIRouter

from database.crud import create_user, get_or_create_user, get_user, get_all_users, edit_user
from database.models.pydantic import UserModel

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/users", description="Получить всех пользователей", name="Get Users")
async def getUsers() -> list[UserModel] | None:
    users = get_all_users()

    return [user.__data__ for user in users] if users else None


@router.get("/{tg_id}", description="Получить пользователя по tg_id", name="Get User")
async def getUser(tg_id: str):
    user = get_user(tg_id=tg_id)

    return user.__data__ if user else None


@router.post("/create_user", description="Создать пользователя", name="Create User")
async def createUser(user_data: UserModel):
    user = create_user(user_data=user_data)

    return user.__data__ if user else None


@router.post("/get_or_create_user", description="Получить или создать пользователя", name="Get or create User")
async def getOrCreateUser(user_data: UserModel):
    user = get_or_create_user(user_data=user_data)

    return user.__data__ if user else None


@router.post("/edit_user", description="Редактировать пользователя", name="Edit User")
async def editUser(user_data: UserModel) -> bool:
    res = edit_user(user_data=user_data)

    return res
