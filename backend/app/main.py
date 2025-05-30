from fastapi import FastAPI
from pydantic import BaseModel
from app.routes import sensors
from app.routes import readings

app = FastAPI()
app.include_router(sensors.router, prefix="/api")
app.include_router(readings.router, prefix="/readings")