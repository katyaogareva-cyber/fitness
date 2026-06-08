from sqlalchemy.orm import Session
from app import models, schemas
from sqlalchemy.orm import joinedload



def get_bookings(db: Session):
    return (
        db.query(models.Booking)
        .options(
            joinedload(models.Booking.user),
            joinedload(models.Booking.workout)
        )
        .all()
    )


def get_bookings(db: Session):
    return db.query(models.Booking).all()
