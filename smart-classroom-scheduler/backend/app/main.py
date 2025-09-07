import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from . import models
from .routers import teachers, rooms, subjects, timeslots, scheduler

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Classroom & Timetable Scheduler API")

origins = os.getenv("ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(teachers.router)
app.include_router(rooms.router)
app.include_router(subjects.router)
app.include_router(timeslots.router)
app.include_router(scheduler.router)

@app.get("/health")
def health():
    return {"status": "ok"}
