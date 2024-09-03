from fastapi import APIRouter

from database.crud import create_ps, get_ps, get_all_ps, edit_ps
from database.models.pydantic import PSModel

router = APIRouter(prefix="/ps", tags=["ps"])


@router.get("/pss", name="Get all PS", description="Получить все PS")
async def getAllPs():
    pss = get_all_ps()

    return [ps.to_dict() for ps in pss] if pss else None


@router.get("/{ps_id}", name="Get PS", description="Получить PS")
async def getPs(ps_id: int):
    ps = get_ps(ps_id=ps_id)

    return ps.to_dict() if ps else None


@router.post("/edit_ps", name="Edit PS", description="Изменить PS")
async def editPs(ps: PSModel):
    result = edit_ps(ps=ps)

    return result
