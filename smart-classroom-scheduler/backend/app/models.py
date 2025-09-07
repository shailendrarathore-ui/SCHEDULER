from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, UniqueConstraint, Boolean
from .database import Base

class Teacher(Base):
    __tablename__ = "teachers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)

class Room(Base):
    __tablename__ = "rooms"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    has_projector: Mapped[bool] = mapped_column(Boolean, default=False)
    is_lab: Mapped[bool] = mapped_column(Boolean, default=False)

class Subject(Base):
    __tablename__ = "subjects"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    requires_lab: Mapped[bool] = mapped_column(Boolean, default=False)

class TimeSlot(Base):
    __tablename__ = "timeslots"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    label: Mapped[str] = mapped_column(String, unique=True, index=True)  # e.g., "Mon-09:00"
    day_index: Mapped[int] = mapped_column(Integer)  # 0..6
    slot_index: Mapped[int] = mapped_column(Integer)  # 0..N in a day
    __table_args__ = (UniqueConstraint("day_index", "slot_index", name="uq_day_slot"),)

class Assignment(Base):
    __tablename__ = "assignments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    timeslot_id: Mapped[int] = mapped_column(ForeignKey("timeslots.id"))
    __table_args__ = (UniqueConstraint("room_id", "timeslot_id", name="uq_room_slot"),
                      UniqueConstraint("teacher_id", "timeslot_id", name="uq_teacher_slot"))
