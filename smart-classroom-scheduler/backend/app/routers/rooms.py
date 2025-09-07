from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/rooms", tags=["rooms"])

@router.get("/", response_model=list[schemas.Room])
def list_rooms(db: Session = Depends(get_db)):
    return db.query(models.Room).all()

@router.post("/", response_model=schemas.Room)
def create_room(payload: schemas.RoomCreate, db: Session = Depends(get_db)):
    if db.query(models.Room).filter_by(name=payload.name).first():
        raise HTTPException(400, "Room already exists")
    r = models.Room(**payload.model_dump())
    db.add(r); db.commit(); db.refresh(r)
    return r
