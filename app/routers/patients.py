from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, crud, database, auth, models

router = APIRouter()

@router.post("/patients/", response_model=schemas.PatientRead)
def create_patient(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    # Only allow users with role 'patient' to create a patient profile
    if current_user.role != "patient":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    # Check if patient profile already exists
    existing = crud.get_patient(db, current_user.id)
    if existing:
        raise HTTPException(status_code=400, detail="Patient profile already exists")
    return crud.create_patient(db, user_id=current_user.id)

@router.get("/patients/{patient_id}", response_model=schemas.PatientRead)
def get_patient(patient_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    patient = crud.get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.get("/patients/{patient_id}/records", response_model=list[schemas.MedicalRecordRead])
def get_patient_records(patient_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    # Only allow the patient or a doctor to view records
    if current_user.role not in ["patient", "doctor"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    if current_user.role == "patient" and current_user.id != patient_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    return crud.get_medical_records_by_patient(db, patient_id)