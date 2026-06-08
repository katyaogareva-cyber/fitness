from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


# ---------- USER ----------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    bookings = relationship("Booking", back_populates="user")


# ---------- WORKOUT ----------
class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)

    bookings = relationship("Booking", back_populates="workout")


# ---------- BOOKING ----------
class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    workout_id = Column(Integer, ForeignKey("workouts.id"))

    user = relationship("User", back_populates="bookings")
    workout = relationship("Workout", back_populates="bookings")
