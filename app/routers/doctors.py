from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, crud, database, auth, models

router = APIRouter()

@router.post("/doctors/", response_model=schemas.DoctorRead)
def create_doctor(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
	# Only allow users with role 'doctor' to create a doctor profile
	if current_user.role != "doctor":
		raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
	# Check if doctor profile already exists
	existing = crud.get_doctor(db, current_user.id)
	if existing:
		raise HTTPException(status_code=400, detail="Doctor profile already exists")
	return crud.create_doctor(db, user_id=current_user.id)

@router.get("/doctors/{doctor_id}", response_model=schemas.DoctorRead)
def get_doctor(doctor_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
	doctor = crud.get_doctor(db, doctor_id)
	if not doctor:
		raise HTTPException(status_code=404, detail="Doctor not found")
	return doctor
