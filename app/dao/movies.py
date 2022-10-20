from app.dao.model.movies import Movie


class MoviesDAO():
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_id(self, mid):
        return self.session.query(Movie).get(mid)

    def get_by_director(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did)

    def get_by_year(self, yid):
        return self.session.query(Movie).filter(Movie.year == yid)

    def get_by_genre(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid)

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

    def update(self, data):
        self.session.add(data)
        self.session.commit()

    def delete(self, mid):
        movie = self.get_by_id(mid)
        self.session.delete(movie)
        self.session.commit()
