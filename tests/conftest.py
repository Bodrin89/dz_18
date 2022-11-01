
import pytest

from unittest.mock import MagicMock

from app.dao.director import DirectorDAO
from app.dao.model.director import Director
from app.dao.model.genre import Genre
from app.dao.genre import GenreDAO
from app.dao.model.movies import Movie
from app.dao.movies import MoviesDAO


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name='тестовый жанр 1')
    genre_2 = Genre(id=2, name='тестовый жанр 2')
    genre_3 = Genre(id=3, name='тестовый жанр 3')

    genre_dao.get_by_id = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])
    genre_dao.create = MagicMock(return_value=Genre(id=55, name="тестовый жанр 55"))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao

@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director_1 = Director(id=1, name='тестовый режиссер 1')
    director_2 = Director(id=2, name='тестовый режиссер 2')
    director_3 = Director(id=3, name='тестовый режиссер 3')

    director_dao.get_by_id = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=[director_1, director_2, director_3])
    director_dao.create = MagicMock(return_value=Director(id=55, name="тестовый режиссер 55"))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MoviesDAO(None)

    movie_1 = Movie(id=1, title='тестовый фильм 1', description='тестовое описание', trailer="trailer", year=2022,
                     rating=8.0, genre_id="genre_id", director_id="director_id")
    movie_2 = Movie(id=2, title='тестовый фильм 2', description='тестовое описание', trailer="trailer", year=2022,
                     rating=8.0, genre_id="genre_id", director_id="director_id")
    movie_3 = Movie(id=3, title='тестовый фильм 3', description='тестовое описание', trailer="trailer", year=2022,
                     rating=8.0, genre_id="genre_id", director_id="director_id")
    director_1 = Director(id=1, name='тестовый режиссер 1')
    genre_1 = Genre(id=1, name='тестовый жанр 1')

    movie_dao.get_by_id = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create = MagicMock(return_value=Movie(id=55, title='тестовый фильм 55', description='тестовое описание',
                                                     trailer="trailer", year=2022,
                     rating=8.0, genre_id="genre_id", director_id="director_id"))
    movie_dao.get_by_director = MagicMock(return_value=director_1)
    movie_dao.get_by_genre = MagicMock(return_value=genre_1)
    movie_dao.get_by_year = MagicMock(return_value=Movie(year=2022))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao


