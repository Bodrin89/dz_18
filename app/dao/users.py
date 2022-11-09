
from app.dao.model.users import User

class UserDAO():
    def __init__(self, session):
        self.session = session

    def get_user(self, password, email):
        """Получение юзера по паролю и email"""
        return self.session.query(User).filter(User.email == email, User.password == password).first()

    def get_user_id(self, uid):
        """Получение юзера по id"""
        return self.session.query(User).filter(User.id == uid).first()

    def update_user(self, data, dict_update):
        """Обновление имени, фамилии, любимого жанра пользователя"""
        self.session.query(User).filter(User.id == data['id']).update(dict_update)
        self.session.commit()

    def update_password(self, data, dict_update):
        self.session.query(User).filter(User.id == data['id']).update(dict_update)
        self.session.commit()





