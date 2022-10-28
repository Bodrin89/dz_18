from app.dao.model.director import Director


class DirectorDAO():
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """Получение всех режиссеров"""
        return self.session.query(Director).all()

    def get_by_id(self, did):
        """Получение режиссера по id"""
        return self.session.query(Director).get(did)

    def create(self, data):
        """Создание нового режиссера"""
        director = Director(**data)
        self.session.add(director)
        self.session.commit()

    def update(self, data):
        """Обновление данных в режиссере"""
        self.session.add(data)
        self.session.commit()

    def delete(self, did):
        """Удаление режиссера"""
        director = self.get_by_id(did)
        self.session.delete(director)
        self.session.commit()

