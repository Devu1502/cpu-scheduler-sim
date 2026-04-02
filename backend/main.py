from fastapi import FastAPI
from backend.routes.scheduler import router as scheduler_router
app = FastAPI()
app.include_router(scheduler_router)