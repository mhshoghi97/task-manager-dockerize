from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import auth, tasks
from app.database import engine
from app.models import user, task



# Create Tables
user.Base.metadata.create_all(bind=engine)
task.Base.metadata.create_all(bind=engine)



app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)



# Include routers
app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth",tags=["auth"])
app.include_router(tasks.router, prefix=f"{settings.API_V1_STR}/tasks",tags=["tasks"])


@app.get("/")
def read_root():
    return {"message": "Welcome to Task Manager API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)