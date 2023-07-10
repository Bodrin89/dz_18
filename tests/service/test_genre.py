
import pytest
from app.services.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_by_id(self):
        genre = self.genre_service.get_by_id(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genre = self.genre_service.get_all()
        assert len(genre) > 0

    def test_created(self):
        genre_data = {"name": "Жанр для теста"}
        genre = self.genre_service.create(genre_data)
        assert genre.id and genre.name is not None

    def test_update(self):
        genre_data = {"name": "Жанр для теста"}
        self.genre_service.update(genre_data)

    def test_delete(self):
        self.genre_service.delete(1)

