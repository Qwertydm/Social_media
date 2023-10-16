from fastapi import APIRouter


profile_router = APIRouter(prefix='/profile', tags=['Профиль пользователей'])

from profile import profile_api