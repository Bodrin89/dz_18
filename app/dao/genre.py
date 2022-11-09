
from app.dao.model.genre import Genre


class GenreDAO():
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """Получение всех жанров"""
        return self.session.query(Genre).all()

    def get_page(self, slice_argument):
        """Получение жанра по страницам"""
        return self.session.query(Genre).slice(slice_argument[0], slice_argument[1])

    def get_by_id(self, gid):
        """Получение жанра по id"""
        return self.session.query(Genre).get(gid)

    def create(self, data):
        """Создание нового жанра"""
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()

    def update(self, data):
        """Обновление данных в жанре"""
        self.session.add(data)
        self.session.commit()

    def delete(self, gid):
        """Удаление жанра"""
        genre = self.get_by_id(gid)
        self.session.delete(genre)
        self.session.commit()

