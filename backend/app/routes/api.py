from fastapi import APIRouter
from datetime import datetime
from pydantic import BaseModel

router = APIRouter()

class ReadingIn(BaseModel):
  sensor_id : str
  value : float
  timestamp : datetime

@router.get("/")
def root():
  return {"msg": "API is running"}

@router.get("/sensors")
def get_sensors():
  return {"msg": "Sensors are running"}

@router.post("/readings")
def create_reading(reading: ReadingIn):
  print(reading)
  return {"msg": "received", "data": reading}