from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/check")
async def healthcheck():
    return {"status": "ok", "message": "Connection stabilized"}
