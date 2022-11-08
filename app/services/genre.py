
from app.dao.genre import GenreDAO
from utils.funcs import pagination

class GenreService():
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self):
        """Получение всех жанров"""
        return self.dao.get_all()

    def get_page(self, page_number):
        list_pages = pagination()
        slice_argument = list_pages[page_number - 1]  # Кортеж из аргументов для запроса к БД
        return self.dao.get_page(slice_argument)

    def get_by_id(self, gid):
        """Получение жанра по id"""
        return self.dao.get_by_id(gid)

    def create(self, data):
        """Создание нового жанра"""
        return self.dao.create(data)

    def update(self, data):
        """Обновление данных в жанре"""
        gid = data.get('id')
        genre = self.get_by_id(gid)
        genre.name = data.get('name')
        self.dao.update(genre)

    def delete(self, gid):
        """Удаление жанра"""
        self.dao.delete(gid)

