# Fitness Club API (FastAPI)

Simple backend project for a fitness club management system.

## Features

- Create and get users
- Create and get workouts
- Book workouts for users
- Validation:
  - user must exist
  - workout must exist
  - no duplicate bookings

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

## How to run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
