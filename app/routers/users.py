from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app import models, schemas, crud, database, auth
from app.logger import logger

router = APIRouter()

@router.post("/register", response_model=schemas.UserRead)
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user: 
        raise HTTPException(status_code=400, detail="Username already registered")
    db_email = crud.get_user_by_email(db, user.email)
    if db_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = auth.get_password_hash(user.password)
    new_user = crud.create_user(db, user, hashed_password)
    return new_user

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    logger.info("Login attempt for user: %s", form_data.username)
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        logger.warning("Failed login for user: %s", form_data.username)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(data={"sub": user.username, "role": user.role})
    logger.info("Login successful for user: %s", form_data.username)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=schemas.UserRead)
def read_users_me(current_user: models.User = Depends(auth.get_current_user)):
    return current_user