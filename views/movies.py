
from flask import request
from flask_restx import Resource, Namespace

from app.conteiner import movie_service
from app.dao.model.movies import MovieSchema
from utils.decorators import auth_required, admin_required

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movie_ns.route('/')
class MoviesViews(Resource):
    @auth_required
    def get(self):
        all_movies = movie_service.get_all()
        return movies_schema.dump(all_movies), 200

    @admin_required
    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return 'Создано', 201


@movie_ns.route('/directors/<int:did>')
class MovieViews(Resource):
    def get(self, did: int):
        movie_director = movie_service.get_by_director(did)
        return movies_schema.dump(movie_director), 200


@movie_ns.route('/genres/<int:gid>')
class MovieViews(Resource):
    def get(self, gid: int):
        movie_genre = movie_service.get_by_genre(gid)
        return movies_schema.dump(movie_genre), 200

@movie_ns.route('/years/<int:yid>')
class MovieViews(Resource):
    def get(self, yid: int):
        movie_year = movie_service.get_by_year(yid)
        return movies_schema.dump(movie_year)


@movie_ns.route('/<int:mid>')
class MovieViews(Resource):
    @auth_required
    def get(self, mid: int):
        movie = movie_service.get_by_id(mid)
        return movie_schema.dump(movie), 200

    @admin_required
    def put(self, mid: int):
        req_json = request.json
        req_json['id'] = mid
        movie_service.update(req_json)
        return "Обновленно", 200

    @admin_required
    def delete(self, mid: int):
        movie_service.delete(mid)
        return "Удалено", 200




