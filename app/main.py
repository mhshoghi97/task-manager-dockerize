from fastapi import FastAPI
from app.core.security import get_password_hash
# from fastapi.middleware.cors import CORSMiddleware
# from app.core.config import settings
# from app


app = FastAPI(title="Task Management Simple Service")


@app.get("/")
async def root():
    hashed_password = get_password_hash("password")
    return {"message": "Hello World", "hashed_password": hashed_password}