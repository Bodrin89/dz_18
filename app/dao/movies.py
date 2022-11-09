from app.dao.model.movies import Movie


class MoviesDAO():
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """Получение всех фильмов"""
        return self.session.query(Movie).all()

    def get_page(self, slice_argument, status):
        """ Получение записей на заданной странице"""
        if status == True:
            # Получение записей с сортировкой по году
            return self.session.query(Movie).order_by(-Movie.year).slice(slice_argument[0], slice_argument[1])
        # Без сортировки по году
        return self.session.query(Movie).slice(slice_argument[0], slice_argument[1])

    def get_by_id(self, mid):
        """Получить фильм по id"""
        return self.session.query(Movie).get(mid)

    def create(self, data):
        """Создать фильм"""
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

    def update(self, data):
        """Обновить фильм"""
        self.session.add(data)
        self.session.commit()

    def delete(self, mid):
        """Удалить фильм"""
        movie = self.get_by_id(mid)
        self.session.delete(movie)
        self.session.commit()
