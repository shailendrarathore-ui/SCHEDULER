from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/teachers", tags=["teachers"])

@router.get("/", response_model=list[schemas.Teacher])
def list_teachers(db: Session = Depends(get_db)):
    return db.query(models.Teacher).all()

@router.post("/", response_model=schemas.Teacher)
def create_teacher(payload: schemas.TeacherCreate, db: Session = Depends(get_db)):
    if db.query(models.Teacher).filter_by(name=payload.name).first():
        raise HTTPException(400, "Teacher already exists")
    t = models.Teacher(name=payload.name)
    db.add(t); db.commit(); db.refresh(t)
    return t
