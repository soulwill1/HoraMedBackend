from fastapi import APIRouter

from app.api.v1.auth.routes.auth_routes import api_auth as auth_router
from app.api.v1.users.routes.user_create_routes import api_users as users_router


api_router = APIRouter()

api_router.include_router(auth_router,tags=["auth"])
api_router.include_router(users_router, tags=["users"])