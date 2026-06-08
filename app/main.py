from fastapi import FastAPI
from app.database import Base, engine

from app.routers import users, workouts, bookings

app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(users.router)
app.include_router(workouts.router)
app.include_router(bookings.router)


@app.get("/")
def root():
    return {"message": "Fitness API"}
