from pydantic import BaseModel


# USER
class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    pass


class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True


# WORKOUT
class WorkoutBase(BaseModel):
    title: str


class WorkoutCreate(WorkoutBase):
    pass


class WorkoutOut(WorkoutBase):
    id: int

    class Config:
        from_attributes = True


# BOOKING
class BookingBase(BaseModel):
    user_id: int
    workout_id: int


class BookingCreate(BookingBase):
    pass

class BookingOut(BaseModel):
    id: int
    user: UserOut
    workout: WorkoutOut

    class Config:
        from_attributes = True
