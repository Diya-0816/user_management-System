from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    email: EmailStr
    username: str | None = None
    is_verified: bool
    class Config:
        orm_mode = True
