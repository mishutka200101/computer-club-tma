import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from routes import ps_router, user_router, booking_router, health_router

from database import init

links = [
    "http://localhost",
    "http://localhost:5174",
    "https://localhost:5174"
]

init()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=links,
    allow_methods=["*"],
    allow_headers=["*"]
)
main_router = APIRouter(prefix='/api')
main_router.include_router(ps_router)
main_router.include_router(user_router)
main_router.include_router(booking_router)
main_router.include_router(health_router)
app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
