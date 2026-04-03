from fastapi import FastAPI
from app import model
from app.database import engine
from app.routers import records, dashbord
model.Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Finance Dashboard API",
    description="A backend API for managing financial records with role-based access control.",
    version="1.0.0"
)
app.include_router(records.router)
app.include_router(dashbord.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Finance Dashboard API! Go to /docs to test the endpoints."}