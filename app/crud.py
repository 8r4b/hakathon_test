from sqlalchemy.orm import Session
from app import models, schemas
from typing import Optional, List

# User CRUD
def get_user_by_username(db: Session, username: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate, hashed_password: str) -> models.User:
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        is_active=True,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Patient CRUD
def create_patient(db: Session, user_id: int) -> models.Patient:
    db_patient = models.Patient(user_id=user_id)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patient(db: Session, patient_id: int) -> Optional[models.Patient]:
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

# Doctor CRUD
def create_doctor(db: Session, user_id: int) -> models.Doctor:
    db_doctor = models.Doctor(user_id=user_id)
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def get_doctor(db: Session, doctor_id: int) -> Optional[models.Doctor]:
    return db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()

# MedicalRecord CRUD
def create_medical_record(db: Session, record: schemas.MedicalRecordCreate) -> models.MedicalRecord:
    db_record = models.MedicalRecord(
        patient_id=record.patient_id,
        doctor_id=record.doctor_id,
        symptoms=record.symptoms,
        diagnosis=record.diagnosis
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def get_medical_record(db: Session, record_id: int) -> Optional[models.MedicalRecord]:
    return db.query(models.MedicalRecord).filter(models.MedicalRecord.id == record_id).first()

def get_medical_records_by_patient(db: Session, patient_id: int) -> List[models.MedicalRecord]:
    return db.query(models.MedicalRecord).filter(models.MedicalRecord.patient_id == patient_id).all()