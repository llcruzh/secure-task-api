from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserCreate, UserOut
from app.schemas.token import TokenOut
from app.services.auth import register_user, login_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserOut, status_code=201)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    try:
        return register_user(db, payload.email, payload.password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=TokenOut)
def login(payload: UserCreate, db: Session = Depends(get_db)):
    # reusing UserCreate for email+password input
    try:
        token = login_user(db, payload.email, payload.password)
        return TokenOut(access_token=token)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
