from fastapi import FastAPI
from . import models
from .database import engine
from .routes import notes

# 1. Create Database Tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Simple Note Taking App",
    description="A basic API to learn FastAPI and Pydantic",
    version="1.0.0"
)

# 2. Include Routers
app.include_router(notes.router)

# 3. Root Endpoint (Health Check)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Note Taking API! Go to /docs for Swagger UI"}