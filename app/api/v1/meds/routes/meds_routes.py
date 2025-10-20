from fastapi import APIRouter


api_meds = APIRouter(
    prefix="/medications",
)

@api_meds.get("/")
def root():
    return {"message": "API running 🚀"}