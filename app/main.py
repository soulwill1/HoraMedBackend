from fastapi import FastAPI
from .db import models, database
from .api.auth.routes import routes

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Auth API with Cookies")

app.include_router(routes.router)

@app.get("/")
def root():
    return {"message": "API running 🚀"}
