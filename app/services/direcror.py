
from app.dao.director import DirectorDAO

class DirectorService():
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self):
        """Получение всех режиссеров"""
        return self.dao.get_all()

    def get_by_id(self, did):
        """Получение режиссера по id"""
        return self.dao.get_by_id(did)

    def create(self, data):
        """Создание нового режиссера"""
        return self.dao.create(data)

    def update(self, data):
        """Обновление данных в режиссере"""
        did = data.get('id')
        director = self.get_by_id(did)
        director.name = data.get('name')
        self.dao.update(director)

    def delete(self, did):
        """Удаление режиссера"""
        self.dao.delete(did)

