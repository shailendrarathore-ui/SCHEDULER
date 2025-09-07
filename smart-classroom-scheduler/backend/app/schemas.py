from pydantic import BaseModel

class TeacherBase(BaseModel):
    name: str

class TeacherCreate(TeacherBase): pass

class Teacher(TeacherBase):
    id: int
    class Config: from_attributes = True

class RoomBase(BaseModel):
    name: str
    has_projector: bool = False
    is_lab: bool = False

class RoomCreate(RoomBase): pass

class Room(RoomBase):
    id: int
    class Config: from_attributes = True

class SubjectBase(BaseModel):
    name: str
    requires_lab: bool = False

class SubjectCreate(SubjectBase): pass

class Subject(SubjectBase):
    id: int
    class Config: from_attributes = True

class TimeSlotBase(BaseModel):
    label: str
    day_index: int
    slot_index: int

class TimeSlotCreate(TimeSlotBase): pass

class TimeSlot(TimeSlotBase):
    id: int
    class Config: from_attributes = True

class Assignment(BaseModel):
    id: int
    subject_id: int
    teacher_id: int
    room_id: int
    timeslot_id: int
    class Config: from_attributes = True
