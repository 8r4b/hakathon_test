from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# User Schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

# Patient Schemas
class PatientBase(BaseModel):
    user_id: int

class PatientRead(PatientBase):
    id: int

    class Config:
        orm_mode = True

# Doctor Schemas
class DoctorBase(BaseModel):
    user_id: int

class DoctorRead(DoctorBase):
    id: int

    class Config:
        orm_mode = True
    
# Medical Record Schemas
class MedicalRecordBase(BaseModel):
    symptoms: str
    diagnosis: Optional[str] = None

class MedicalRecordCreate(MedicalRecordBase):
    patient_id: int
    doctor_id: Optional[int] = None

class MedicalRecordRead(MedicalRecordBase):
    id: int
    patient_id: int
    doctor_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    class Config: 
        orm_mode = True
