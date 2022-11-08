from app.dao.movies import MoviesDAO
from utils.funcs import pagination

class MovieService:
    def __init__(self, dao: MoviesDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_page(self, page_number, status):
        list_pages = pagination()
        slice_argument = list_pages[page_number - 1]  # Кортеж из аргументов для запроса к БД
        if status == True:
            return self.dao.get_page(slice_argument, status)
        return self.dao.get_page(slice_argument, status)

    def get_by_id(self, mid):
        return self.dao.get_by_id(mid)

    def get_by_director(self, did):
        return self.dao.get_by_director(did)

    def get_by_genre(self, gid):
        return self.dao.get_by_genre(gid)

    def get_by_year(self, yid):
        return self.dao.get_by_year(yid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get('id')
        movie = self.get_by_id(mid)
        movie.year = data.get('year')
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.rating = data.get('rating')
        movie.trailer = data.get('trailer')
        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)
