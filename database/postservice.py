from database.models import PostPhoto, UserPost
from database import get_db

# Получить все публикации
def get_all_posts_db():
    db = next(get_db())

    all_posts = db.query(UserPost).all()

    return all_posts

# Получить определенную публикацию
def get_exact_post_db(post_id):
    db = next(get_db())

    # Запрос в базу данных на получение определенного поста по его id
    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        return exact_post

    return "Публикация не найдена"

# Добавить публикацию
def add_new_post_db(user_id, post_text, publish_date):
    db = next(get_db())

    new_post = UserPost(user_id=user_id, post_text=post_text, publish_date=publish_date)

    db.add(new_post)
    db.commit()

    return new_post.post_id

# Изменить текст к публикации
def edit_post_text_db(post_id, new_text):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        exact_post.post_text = new_text
        db.commit()

        return "Текст публикации изменен"

    return "Пост не найден"


# Удалить публикацию
def delete_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        db.delete(exact_post)
        db.commit()

        return "Пост удален"

    return "Пост не найден"

# Загрузить фотографии определенного поста
def upload_post_photo_db(post_id, photo_path):
    db = next(get_db())

    new_photo = PostPhoto(post_id=post_id, photo_path=photo_path)

    db.add(new_photo)
    db.commit()

    return "Фото добавлено к публикации"

# Добавить лайк к публикации
def like_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        exact_post.likes += 1
        db.commit()

        return True

    return "Пост не найден"


# Убрать лайк
def unlike_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        exact_post.likes -= 1
        db.commit()

        return True

    return "Пост не найден"

