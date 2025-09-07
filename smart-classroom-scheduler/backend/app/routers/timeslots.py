from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/timeslots", tags=["timeslots"])

@router.get("/", response_model=list[schemas.TimeSlot])
def list_timeslots(db: Session = Depends(get_db)):
    return db.query(models.TimeSlot).order_by(models.TimeSlot.day_index, models.TimeSlot.slot_index).all()

@router.post("/", response_model=schemas.TimeSlot)
def create_timeslot(payload: schemas.TimeSlotCreate, db: Session = Depends(get_db)):
    if db.query(models.TimeSlot).filter_by(day_index=payload.day_index, slot_index=payload.slot_index).first():
        raise HTTPException(400, "Timeslot already exists for this day/slot")
    t = models.TimeSlot(**payload.model_dump())
    db.add(t); db.commit(); db.refresh(t)
    return t
