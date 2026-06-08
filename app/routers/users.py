from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, crud
from app.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@router.get("")
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)
