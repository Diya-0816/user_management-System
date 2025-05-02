from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash
from app.utils.username_generator import generate_unique_username
from sqlalchemy.orm import Session

def create_user(db: Session, data: UserCreate):
    user = User(
        email=data.email,
        hashed_password=get_password_hash(data.password),
        username=generate_unique_username(db)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
