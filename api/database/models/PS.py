from peewee import CharField, AutoField

from database.models.Base import BaseModel


class PS(BaseModel):
    id = AutoField()
    status = CharField(max_length=50, default="FREE")
