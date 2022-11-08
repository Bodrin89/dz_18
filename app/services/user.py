from app.dao.model.users import User
from app.dao.users import UserDAO

class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_user(self, password, email):
        """Получение юзера по паролю и email"""
        return self.dao.get_user(password, email)

    def get_user_id(self, uid):
        """Получение юзера по id"""
        return self.dao.get_user_id(uid)

    def update_user(self, data, user):
        """Обновление имени, фамилии, любимого жанра пользователя"""
        dict_update = {
            User.name: data.get("name", user.name),
            User.surname: data.get("surname", user.surname),
            User.favorite_genre: data.get("favorite_genre", user.favorite_genre)
        }
        return self.dao.update_user(data, dict_update)
