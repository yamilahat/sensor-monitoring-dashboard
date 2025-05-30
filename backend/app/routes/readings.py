from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

class ReadingIn(BaseModel):
  sensor_id : str
  value : float
  timestamp : datetime

router = APIRouter()


@router.get("/")
def root():
  return {"message": "Readings running"}

@router.post("/")
def create_reading(reading: ReadingIn):
  print(reading)
  return {"msg": "received", "data": reading}