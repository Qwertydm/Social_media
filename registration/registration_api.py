from registration import user_router, RegisterModel, LoginModel
from database.userservice import add_new_user, login_user_db, delete_user_db




# Запрос на регистрацию пользователь
@user_router.post('/register-user')
def register_user(data: RegisterModel):
    # Перевод класса на параметры для функции
    register_data = data.model_dump()
    result = add_new_user(**register_data)

    return {'status': 1, 'message': result}

# Запрос на вход в аккаунт
@user_router.post('/login')
def login_user(data: LoginModel):
    login_data = data.model_dump()
    result = login_user_db(**login_data)

    return {'status': 1, 'message': result}

# Запрос на удаление пользователя из базы
@user_router.post('/delete')
def delete_user(user_id: int):
    result = delete_user_db(user_id)

    return {'status': 1, 'message': result}
