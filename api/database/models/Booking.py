from peewee import CharField, IntegerField, ForeignKeyField, DateTimeField, AutoField
from datetime import datetime

from database.models.User import User
from database.models.Base import BaseModel


class Booking(BaseModel):
    id = AutoField()
    seat_number = IntegerField()
    seat_type = CharField(max_length=50)
    status = CharField(max_length=50, default="ACTIVE")
    start_date = DateTimeField()
    end_date = DateTimeField(null=True)
    created_at = DateTimeField(default=datetime.now)
    created_by = ForeignKeyField(User, backref="user_bookings")
