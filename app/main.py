from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app import models
from app.routers import patients, doctors, records, users

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Secure Medical Diagnosis Assistant",
    description="Backend API for medical diagnosis with authentication and OpenAI integration.",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Secure Medical Diagnosis Assistant API"}

# Include routers (uncomment and add as you create them)
app.include_router(users.router)
app.include_router(patients.router)
app.include_router(doctors.router)
app.include_router(records.router)


