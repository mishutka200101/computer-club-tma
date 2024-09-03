from peewee import CharField, DateTimeField
from datetime import datetime

from database.models.Base import BaseModel


class User(BaseModel):
    tg_id = CharField(primary_key=True)
    username = CharField(max_length=255, null=True)
    priveleges = CharField(max_length=50, default="USER")
    created_at = DateTimeField(default=datetime.now)
