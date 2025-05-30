from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
  return {"message": "Sensor API running"}