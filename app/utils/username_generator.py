import random, string
from app.models.user import User
from sqlalchemy.orm import Session

nouns = ["tiger", "lion"]
verbs = ["runs", "jumps"]

def generate_random_username():
    return f"{random.choice(nouns)}_{random.choice(verbs)}_{random.randint(100,999)}"

def generate_unique_username(db: Session):
    for _ in range(10):
        username = generate_random_username()
        if not db.query(User).filter(User.username == username).first():
            return username
    raise Exception("Could not generate unique username.")
