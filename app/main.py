from fastapi import FastAPI
from db.database import Base, engine
from api.auth.routes.auth_routes import api_auth
from api.users.routes.user_create_routes import api_users


app = FastAPI(title="Auth API with Cookies")

Base.metadata.create_all(bind=engine)

app.include_router(api_auth)
app.include_router(api_users)

@app.get("/")
def root():
    return {"message": "API running 🚀"}
