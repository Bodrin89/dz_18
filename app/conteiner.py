
from app.database import db

from app.dao.movies import MoviesDAO
from app.dao.genre import GenreDAO
from app.dao.director import DirectorDAO
from app.dao.users import UserDAO

from app.services.movie import MovieService
from app.services.genre import GenreService
from app.services.direcror import DirectorService
from app.services.user import UserService
from app.services.auth import AuthService


movie_dao = MoviesDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)

auth_service = AuthService(user_service)
