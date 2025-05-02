from fastapi import FastAPI
from app.api.user_router import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/api/users")

@app.get("/")
def read_root():
    return {"message": "Welcome to User Management System"}
