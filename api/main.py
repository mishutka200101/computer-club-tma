import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from routes import ps_router, user_router, booking_router, health_router

from database.init import init_db

# Initialize database
init_db()

# Initialize FastAPI
app = FastAPI(
    docs_url='/api/docs',
    redoc_url='/api/redoc',
)

# Enable CORS
links = [
    "http://localhost",
    "http://localhost:5174",
    "https://localhost:5174"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=links,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Define main router
main_router = APIRouter(prefix='/api')
# Include other routers
main_router.include_router(ps_router)
main_router.include_router(user_router)
main_router.include_router(booking_router)
main_router.include_router(health_router)
# Connect main router to app
app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
