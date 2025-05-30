from fastapi import FastAPI
from app.routes import sensors

app = FastAPI()
app.include_router(sensors.router, prefix="/api")