from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
import app.schemas as schemas
import app.crud as crud

router = APIRouter(prefix="/workouts", tags=["Workouts"])


@router.get("/")
def get_workouts(db: Session = Depends(get_db)):
    return crud.get_workouts(db)


@router.post("/")
def create_workout(workout: schemas.WorkoutCreate, db: Session = Depends(get_db)):
    return crud.create_workout(db, workout)
