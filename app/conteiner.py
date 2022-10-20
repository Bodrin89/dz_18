
from app.database import db

from app.dao.movies import MoviesDAO
from app.dao.genre import GenreDAO
from app.dao.director import DirectorDAO

from app.services.movie import MovieService
from app.services.genre import GenreService
from app.services.direcror import DirectorService


movie_dao = MoviesDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)