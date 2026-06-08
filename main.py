from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()

users = []
workouts = []
bookings = []

user_id_counter = 1
workout_id_counter = 1
booking_id_counter = 1

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
    global user_id_counter

    user.id = user_id_counter
    user_id_counter += 1

    users.append(user)
    return user

@app.get("/users")
def get_users():
    return users

@app.put("/users/{user_id}")
def update_users(user_id: int, new_user: User):
    for user in users:
        if user_id == user.id:
            user.name = new_user.name
            return user
    raise(HTTPException(status_code = 404, detail= "User not found"))

@app.delete("/users/{user_id}")
def delete_users(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return "User remove"
    raise(HTTPException(status_code = 404, detail= "User not found"))

@app.get("/workouts")
def get_workouts():
    return workouts

@app.post("/workouts")
def create_workout(workout:Workout):
    global workout_id_counter

    workout.id = workout_id_counter
    workout_id_counter +=1

    workouts.append(workout)
    return workout

@app.put("/workouts/{workout_id}")
def update_workout(workout_id: int, new_workout: Workout):
    for workout in workouts:
        if workout.id == workout_id:
            workout.title = new_workout.title
            return workout
    raise(HTTPException(status_code = 404, detail= "Workout not found"))

@app.delete("/workout/{workout_id}")
def delete_workout(workout_id):
    for workout in workouts:
        if workout.id == workout_id:
            workouts.remove(workout)
            return "Workout remove"
    raise(HTTPException(status_code = 404, detail = "Workout not found"))

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
