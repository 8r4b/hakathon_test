from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, crud, database, auth, models
from app.openai_api import get_diagnosis_from_openai

router = APIRouter()

# Only doctors can create medical records, and use OpenAI for diagnosis
@router.post("/records/", response_model=schemas.MedicalRecordRead)
def create_medical_record(
	record: schemas.MedicalRecordCreate,
	db: Session = Depends(database.get_db),
	current_user: models.User = Depends(auth.get_current_user)
):
	if current_user.role != "doctor":
		raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
	# Get AI diagnosis
	ai_diagnosis = get_diagnosis_from_openai(record.symptoms)
	record.diagnosis = ai_diagnosis
	return crud.create_medical_record(db, record)

# Any authenticated user can get a record by ID (add more checks as needed)
@router.get("/records/{record_id}", response_model=schemas.MedicalRecordRead)
def get_medical_record(
	record_id: int,
	db: Session = Depends(database.get_db),
	current_user: models.User = Depends(auth.get_current_user)
):
	record = crud.get_medical_record(db, record_id)
	if not record:
		raise HTTPException(status_code=404, detail="Medical record not found")
	return record
