from database.models import User
from database import get_db

# Получить всех пользователей
def get_all_users_db():
    db = next(get_db())

    all_users = db.query(User).all()

    return all_users

# Получить определенного пользователя
def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        return exact_user

    return False

# Добавить пользователя
def add_new_user(name, surname, email, password, city, birthday, reg_date):
    db = next(get_db())

    cheсker = db.query(User).filter_by(email=email).first()

    if cheсker:
        return "Такой емаил уже зарегестрирован"

    else:
        new_user = User(name=name, surname=surname, email=email, password=password, city=city, birthday=birthday, reg_date=reg_date)

        db.add(new_user)
        db.commit()

        return "Пользователь успешно зарегестрирован"
# Проверка пароля
def login_user_db(email, password):
    db = next(get_db())

    user = db.query(User).filter_by(email=email, password=password).first()

    if user:
        return user

    return "Ошибка авторизации"


# Изменить информацию о пользователе
def edit_user_info_db(user_id, edit_info, new_info):
    db = next(get_db())

    exact_user = get_exact_user_db(user_id)

    if exact_user:
        if edit_info == 'city':
            exact_user.city = new_info

        elif edit_info == 'email':
            exact_user.email = new_info

        elif edit_info == 'password':
            exact_user.password = new_info

        elif edit_info == 'name':
            exact_user.n = new_info

        db.commit()

        return "Данные успешно изменены"

    return "Пользователь не найден"

# Удалить пользователя
def delete_user_db(user_id):
    db = next(get_db())

    user =db.query(User).filter_by(user_id=user_id).first()

    if user:
        db.delete(user)
        db.commit()

        return "Пользователь успешно удален"

    return "Пользователь не найден"

# Добавить фото профиля
def upload_profile_photo_db(user_id, photo_path):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        exact_user.profile_photo = photo_path
        db.commit()

        return "Фото профиля добавлено"

    return "Пользователь не найден"

# Удалить фото профиля
def delete_profile_photo_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        exact_user.profile_photo = 'None'
        db.commit()

        return "Фото профиля удалено"

    return "Пользователь не найден"