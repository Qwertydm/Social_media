from database.models import PostComment
from database import get_db

# Получить все  комментарии определенного поста
def get_exact_post_comment_db(post_id):
    db = next(get_db())

    exact_post_comment = db.query(PostComment).filter_by(post_id=post_id).all()

    return exact_post_comment

# Добавить комментарий
def add_new_comment_db(post_id, user_id, comment_text, publish_date):
    db = next(get_db())

    new_comment = PostComment(post_id=post_id, user_id=user_id, comment_text=comment_text, publish_date=publish_date)

    db.add(new_comment)
    db.commit()

    return "Комментарий добавлен"

# Изменить комментарий
def change_exact_comment_db(comment_id, new_comment_text):
    db = next(get_db())

    exact_comment = db.query(PostComment).filter_by(comment_id=comment_id).first()

    if exact_comment:
        exact_comment.comment_text = new_comment_text
        db.commit()

        return "Текст комментария изменен"

    return "Комментарий не найден"


# Удалить комментарий
def delete_exact_comment_db(comment_id):
    db = next(get_db())

    exact_comment = db.query(PostComment).filter_by(comment_id=comment_id).first()

    if exact_comment:
        db.delete(exact_comment)
        db.commit()

        return "Комментарий удален"

    return "Комментарий не найден"
