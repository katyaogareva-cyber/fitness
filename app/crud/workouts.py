from sqlalchemy.orm import Session
from app import models, schemas


def create_workout(db: Session, workout: schemas.WorkoutCreate):
    db_workout = models.Workout(title=workout.title)
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout


def get_workouts(db: Session):
    return db.query(models.Workout).all()
