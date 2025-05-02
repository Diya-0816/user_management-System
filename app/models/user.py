from sqlalchemy import Column, Integer, String, Boolean
from app.db.base_class import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    username = Column(String, unique=True)
    is_verified = Column(Boolean, default=False)
    is_pro = Column(Boolean, default=False)
    pro_requested = Column(Boolean, default=False)
