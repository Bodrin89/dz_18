
from flask import request
from flask_restx import Resource, Namespace

from app.conteiner import movie_service
from app.dao.model.movies import MovieSchema

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesViews(Resource):

    def get(self):
        data = request.args
        # поиск на странице если указан не обязательный URL-параметр 'page'
        if data.get('page') is not None:

            # Сортировка по году выпуска
            if data.get('status') is not None and data.get('status').lower() == 'new':
                page = movie_service.get_page(int(data.get('page')), status=True)
                return movies_schema.dump(page)
            page = movie_service.get_page(int(data.get('page')), status=False)
            return movies_schema.dump(page)
        all_movies = movie_service.get_all()
        return movies_schema.dump(all_movies), 200

    def post(self):
        """Создать фильм"""
        req_json = request.json
        movie_service.create(req_json)
        return 'Создано', 201

@movie_ns.route('/<int:mid>')
class MovieViews(Resource):

    def get(self, mid: int):
        """Получить фильм по id"""
        movie = movie_service.get_by_id(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid: int):
        """Обновить фильм"""
        req_json = request.json
        req_json['id'] = mid
        movie_service.update(req_json)
        return "Обновленно", 201

    def delete(self, mid: int):
        """Удалить фильм"""
        movie_service.delete(mid)
        return "Удалено", 204




