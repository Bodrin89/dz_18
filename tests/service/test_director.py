
import pytest
from app.services.direcror import DirectorService

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_by_id(self):
        director = self.director_service.get_by_id(1)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        director = self.director_service.get_all()
        assert len(director) > 0

    def test_created(self):

        director_data = {"name": "Режиссер для теста"}
        director = self.director_service.create(director_data)
        assert director.id and director.name is not None

    def test_update(self):
        director_data = {"name": "Режиссер для теста"}
        self.director_service.update(director_data)

    def test_delete(self):
        self.director_service.delete(1)

