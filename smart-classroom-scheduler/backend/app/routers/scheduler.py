from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..services.scheduler import generate_schedule

router = APIRouter(prefix="/scheduler", tags=["scheduler"])

@router.post("/generate")
def generate(db: Session = Depends(get_db)):
    subjects = [ {"id": s.id, "name": s.name, "requires_lab": s.requires_lab} for s in db.query(models.Subject).all() ]
    teachers = [ {"id": t.id, "name": t.name} for t in db.query(models.Teacher).all() ]
    rooms    = [ {"id": r.id, "name": r.name, "is_lab": r.is_lab, "has_projector": r.has_projector} for r in db.query(models.Room).all() ]
    timeslots= [ {"id": ts.id, "label": ts.label, "day_index": ts.day_index, "slot_index": ts.slot_index} for ts in db.query(models.TimeSlot).all() ]

    schedule = generate_schedule(subjects, teachers, rooms, timeslots)

    # Clear previous assignments & insert new
    db.query(models.Assignment).delete()
    for a in schedule:
        db.add(models.Assignment(**a))
    db.commit()

    return {"generated": len(schedule)}

@router.get("/assignments")
def list_assignments(db: Session = Depends(get_db)):
    # Simple joined view
    q = db.query(models.Assignment, models.Subject, models.Teacher, models.Room, models.TimeSlot).join(
        models.Subject, models.Assignment.subject_id == models.Subject.id
    ).join(
        models.Teacher, models.Assignment.teacher_id == models.Teacher.id
    ).join(
        models.Room, models.Assignment.room_id == models.Room.id
    ).join(
        models.TimeSlot, models.Assignment.timeslot_id == models.TimeSlot.id
    ).all()

    results = []
    for a, s, t, r, ts in q:
        results.append({
            "assignment_id": a.id,
            "subject": s.name,
            "teacher": t.name,
            "room": r.name,
            "timeslot": ts.label,
            "day_index": ts.day_index,
            "slot_index": ts.slot_index,
        })
    return results
