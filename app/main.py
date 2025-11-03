from fastapi import FastAPI
from .db.database import Base, engine
from .api.v1.router import api_router
from .core.config import setup_cors


app = FastAPI(title="HoraMed API")

Base.metadata.create_all(bind=engine)


setup_cors(app)
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "API running 🚀"}
