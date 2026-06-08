from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    bookings = relationship("Booking", back_populates="user")


class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)

    bookings = relationship("Booking", back_populates="workout")


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    workout_id = Column(Integer, ForeignKey("workouts.id"))

    user = relationship("User", back_populates="bookings")
    workout = relationship("Workout", back_populates="bookings")
