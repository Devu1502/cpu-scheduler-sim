from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.scheduler import router as scheduler_router
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(scheduler_router)