from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()

users = []
workouts = []
bookings = []

@app.get("/")
def root():
    return {"message": "Hello Fitness Club"}


class User(BaseModel):
    id: int
    name: str

class Workout(BaseModel):
    id: int 
    title: str

class Booking(BaseModel):
    user_id: int
    workout_id: int

@app.post("/users")
def create_user(user:User):
    users.append(user)
    return user

@app.get("/users")
def get_users():
    return users

@app.get("/workouts")
def get_workouts():
    return workouts

@app.post("/workouts")
def create_workout(workout:Workout):
    workouts.append(workout)
    return workout

@app.get("/bookings")
def get_bookings():
    return bookings

@app.post("/bookings")
def create_booking(booking:Booking):
    for user in users:
        if user.id == booking.user_id:
            break
    else: raise HTTPException(status_code=404, detail="User not found")

    for workout in workouts:
        if workout.id == booking.workout_id:
            break
    else: raise HTTPException(status_code=404, detail="Workout not found")

    for b in bookings:
        if b.user_id == booking.user_id and b.workout_id == booking.workout_id:
            raise HTTPException(status_code=400, detail="Booking already exist")

    bookings.append(booking)
    return booking


