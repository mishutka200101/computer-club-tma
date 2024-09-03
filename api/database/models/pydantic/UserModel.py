from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime

PrivelegesType = Literal["USER", "ADMIN"]


class UserModel(BaseModel):
    tg_id: str
    username: Optional[str]
    priveleges: PrivelegesType = "USER"
    created_at: Optional[datetime | str] = datetime.now()
