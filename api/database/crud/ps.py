from database import database
from database.models import PS
from database.models.pydantic import PSModel
from database.utils.decorators import handle_errors


@handle_errors
def create_ps(ps_data: PSModel):
    with database.atomic():
        ps = PS.create(**ps_data.model_dump())
        return ps


@handle_errors
def get_ps(ps_id: int):
    with database.atomic():
        ps = PS.get_by_id(ps_id)
        return ps


@handle_errors
def get_all_ps():
    with database.atomic():
        ps = PS.select()
        return ps


@handle_errors
def edit_ps(ps_data: PSModel):
    with database.atomic():
        res = PS.update(**ps_data.model_dump()
                        ).where(PS.id == ps_data.id).execute()
        return res
