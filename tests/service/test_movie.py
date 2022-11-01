
import pytest
from app.services.movie import MovieService

class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_by_id(self):
        movie = self.movie_service.get_by_id(1)
        assert movie is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_get_by_director(self):
        director = self.movie_service.get_by_director(1)
        assert director is not None

    def test_get_by_genre(self):
        genre = self.movie_service.get_by_genre(1)
        assert genre is not None

    def test_get_by_year(self):
        year = self.movie_service.get_by_year(2002)
        assert year is not None

    def test_create(self):
        movie_data = {"id": 55, "title": "Фильм"}
        movie = self.movie_service.create(movie_data)
        assert movie.id and movie.trailer is not None

    def test_update(self):
        movie_data = {"id": 55, "title": "Фильм"}
        movie = self.movie_service.update(movie_data)

    def test_delete(self):
        movie = self.movie_service.delete(1)






