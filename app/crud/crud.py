from sqlalchemy.orm import Session
import models
import schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(models.User).all()
    

def create_workout(db: Session, workout: schemas.WorkoutCreate):
    db_workout = models.Workout(title=workout.title)
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout


def get_workouts(db: Session):
    return db.query(models.Workout).all()


def create_booking(db: Session, booking: schemas.BookingCreate):
    # проверка user
    user = db.query(models.User).filter(models.User.id == booking.user_id).first()
    if not user:
        return {"error": "User not found"}

    # проверка workout
    workout = db.query(models.Workout).filter(models.Workout.id == booking.workout_id).first()
    if not workout:
        return {"error": "Workout not found"}

    # проверка дубля
    existing = db.query(models.Booking).filter(
        models.Booking.user_id == booking.user_id,
        models.Booking.workout_id == booking.workout_id
    ).first()

    if existing:
        return {"error": "Booking already exists"}

    db_booking = models.Booking(
        user_id=booking.user_id,
        workout_id=booking.workout_id
    )

    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def get_bookings(db: Session):
    return db.query(models.Booking).all()
    
    
def delete_booking(db: Session, booking_id: int):
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    db.delete(booking)
    db.commit()

    return {"message": "Booking deleted"}
