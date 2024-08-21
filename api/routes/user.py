from fastapi import APIRouter

from database import create_user, get_user, get_all_users, get_or_create_user
from models import User

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/users", description="Получить всех пользователей", name="Get Users")
async def getUsers():
    users = get_all_users()

    return [user for user in users] if users else None


@router.get("/{tg_id}", description="Получить пользователя по tg_id", name="Get User")
async def getUser(tg_id: str):
    user = get_user(tg_id=tg_id)

    return user.to_dict() if user else None


@router.post("/", description="Создать пользователя", name="Create User")
async def createUser(user: User):
    result = create_user(user=user)

    return result


@router.post("/get_or_create_user", description="Получить или создать пользователя", name="Get or create User")
async def getOrCreateUser(tg_id: str):
    user = get_or_create_user(tg_id=tg_id)

    return user.to_dict()
