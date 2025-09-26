from fastapi import FastAPI
from .db import models, database
from .api import auth

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Auth API with Cookies")

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "API running 🚀"}
