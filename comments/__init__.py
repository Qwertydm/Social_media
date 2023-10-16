from fastapi import APIRouter

comment_router = APIRouter(prefix='/comments', tags=['Комментарии к публикациям'])

from comments import comments_api
