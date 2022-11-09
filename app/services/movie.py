from app.dao.movies import MoviesDAO
from utils.funcs import pagination

class MovieService:
    def __init__(self, dao: MoviesDAO):
        self.dao = dao

    def get_all(self):
        """Получение всех фильмов"""
        return self.dao.get_all()

    def get_page(self, page_number, status):
        """ Получение записей на заданной странице"""
        list_pages = pagination()
        slice_argument = list_pages[page_number - 1]  # Кортеж из аргументов для запроса к БД
        if status == True:
            return self.dao.get_page(slice_argument, status)  # Получение записей с сортировкой по году
        return self.dao.get_page(slice_argument, status)  # Без сортировки по году

    def get_by_id(self, mid):
        """Получить фильм по id"""
        return self.dao.get_by_id(mid)

    def create(self, data):
        """Создать фильм"""
        return self.dao.create(data)

    def update(self, data):
        """Обновить фильм"""
        mid = data.get('id')
        movie = self.get_by_id(mid)
        movie.year = data.get('year')
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.rating = data.get('rating')
        movie.trailer = data.get('trailer')
        self.dao.update(movie)

    def delete(self, mid):
        """Удалить фильм"""
        self.dao.delete(mid)
