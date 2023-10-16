from fastapi import APIRouter


posts_router = APIRouter(prefix='/post', tags=['Публикации'])

from user_posts import user_posts_api