from app.db.session import SessionLocal
from app.models.user import User
from app.core.security import get_password_hash

def create_admin():
    db = SessionLocal()
    email = input("Enter admin email: ")
    password = input("Enter password: ")
    hashed = get_password_hash(password)
    user = User(email=email, hashed_password=hashed, is_verified=True)
    db.add(user)
    db.commit()
    print("Admin created successfully.")

if __name__ == "__main__":
    create_admin()
