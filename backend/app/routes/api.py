from fastapi import APIRouter
from datetime import datetime
from pydantic import BaseModel

router = APIRouter()
queue = []

class ReadingIn(BaseModel):
  sensor_id : str
  value : float
  timestamp : datetime

@router.get("/")
def root():
  return {"msg": "API is running"}

@router.get("/sensors")
def get_sensors():
  if len(queue) > 0:
    return {"msg": queue.pop(0)}
  return {"msg": "Sensors are running"}

@router.post("/readings")
def create_reading(reading: ReadingIn):
  print(reading)
  queue.append(reading)
  return {"msg": "received", "data": reading}