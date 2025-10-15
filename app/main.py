from fastapi import FastAPI
from .db.database import Base, engine
from .api.v1.router import api_router


app = FastAPI(title="HoraMed API")

Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "API running 🚀"}
