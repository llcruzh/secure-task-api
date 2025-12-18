from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token

def register_user(db: Session, email: str, password: str) -> User:
    existing = db.execute(select(User).where(User.email == email)).scalar_one_or_none()
    if existing:
        raise ValueError("Email already registered.")

    u = User(email=email, password_hash=hash_password(password))
    db.add(u)
    db.commit()
    db.refresh(u)
    return u

def login_user(db: Session, email: str, password: str) -> str:
    u = db.execute(select(User).where(User.email == email)).scalar_one_or_none()
    if not u or not verify_password(password, u.password_hash):
        raise ValueError("Invalid email or password.")
    return create_access_token(subject=str(u.id))
