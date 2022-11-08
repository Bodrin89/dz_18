from flask import request
from flask_restx import Resource, Namespace

from app.conteiner import genre_service
from app.dao.model.genre import GenreSchema

from utils.decorators import auth_required, admin_required

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)



@genre_ns.route('/')
class GenreViews(Resource):

    def get(self):
        """Получение всех жанров"""
        data = request.args
        # поиск на странице если указан не обязательный URL-параметр 'page'
        if data.get('page') is not None:
            page = genre_service.get_page(int(data.get('page')))
            return genres_schema.dump(page)
        all_genre = genre_service.get_all()
        return genres_schema.dump(all_genre), 200


    def post(self):
        """Создание нового жанра"""
        req_json = request.json
        genre_service.create(req_json)
        return 'Создано', 201


@genre_ns.route('/<int:gid>')
class GenreViews(Resource):

    def get(self, gid: int):
        """Получение жанра по id"""
        genre = genre_service.get_by_id(gid)
        return genre_schema.dump(genre)

    def put(self, gid: int):
        """Обновление данных в жанре"""
        req_json = request.json
        req_json['id'] = gid
        genre_service.update(req_json)
        return "Обновленно", 200

    def delete(self, gid: int):
        """Удаление жанра"""
        genre_service.delete(gid)
        return "Удалено", 200

