
from app.dao.model.users import User

class UserDAO():
    def __init__(self, session):
        self.session = session

    def get_by_name(self, user_name):
        return self.session.query(User).filter(User.username == user_name).first()

    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
