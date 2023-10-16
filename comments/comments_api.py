from fastapi import Body
from datetime import datetime

from comments import comment_router
from database.commentservice import get_exact_post_comment_db, add_new_comment_db, delete_exact_comment_db, change_exact_comment_db


# Запрос на получение комментарий к посту (post_id: int)
@comment_router.get('/get-comment')
async def get_exact_post_comment(post_id: int):
    result = get_exact_post_comment_db(post_id)

    return {'status': 1, 'message': result}


# Запрос на добавление комментария (Body)|->(post_id, user_id, comment_text)
@comment_router.post('/add-comment')
async def add_new_comment(post_id: int = Body(...),
                          user_id: int = Body(...),
                          comment_text: str = Body(...)):
    result = add_new_comment_db(post_id=post_id,
                                user_id=user_id,
                                comment_text=comment_text,
                                publish_date=datetime.now())

    return {'status': 1, 'message': result}


# Запрос на изменение текста к комментарию (Body)|->(comment_id, new_comment_text)
@comment_router.put('/edit-comment')
async def change_exact_comment(comment_id: int = Body(...),
                               new_comment_text: str = Body(...)):
    result = change_exact_comment_db(comment_id, new_comment_text)

    return {'status': 1, 'message': result}


# Удаление определенного комментария (comment_id: int)
@comment_router.delete('/delete-comment')
async def delete_exact_comment(comment_id: int):
    result = delete_exact_comment_db(comment_id)

    return {'status': 1, 'message': result}

