from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from database import Base, engine

from user_posts import posts_router
from profile import profile_router
from registration import user_router
from post_photo import photo_router
from comments import comment_router

# Создать базу данных
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')
app.mount(path='/gallery', app=StaticFiles(directory='media'))

# Регистрация компонентов
app.include_router(user_router)
app.include_router(profile_router)
app.include_router(posts_router)
app.include_router(photo_router)
app.include_router(comment_router)
