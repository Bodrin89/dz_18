
from app.dao.model.users import User
from utils.funcs import check_email

class AuthDAO():
    def __init__(self, session):
        self.session = session

    def create(self, data):
        user = User(**data)
        array_email = self.session.query(User.email).all()
        list_email = check_email(array_email)  #Функция получения списка email из БД
        """Проверка совпадения email в БД"""
        try:
            user.email in list_email
            self.session.add(user)
            self.session.commit()
        except Exception as e:
            print(f"Такой email уже есть\n{e}")







