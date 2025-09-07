from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/subjects", tags=["subjects"])

@router.get("/", response_model=list[schemas.Subject])
def list_subjects(db: Session = Depends(get_db)):
    return db.query(models.Subject).all()

@router.post("/", response_model=schemas.Subject)
def create_subject(payload: schemas.SubjectCreate, db: Session = Depends(get_db)):
    if db.query(models.Subject).filter_by(name=payload.name).first():
        raise HTTPException(400, "Subject already exists")
    s = models.Subject(**payload.model_dump())
    db.add(s); db.commit(); db.refresh(s)
    return s
