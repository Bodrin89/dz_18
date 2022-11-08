
from flask import request
from flask_restx import Resource, Namespace

from app.conteiner import director_service
from app.dao.model.director import DirectorSchema
from utils.decorators import auth_required

director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@director_ns.route('/')
class DirectorViews(Resource):
    # @auth_required
    def get(self):
        """Получение всех режиссеров"""
        data = request.args
        # поиск на странице если указан не обязательный URL-параметр 'page'
        if data.get('page') is not None:
            page = director_service.get_page(int(data.get('page')))
            return directors_schema.dump(page)
        all_director = director_service.get_all()
        return directors_schema.dump(all_director), 200

    def post(self):
        """Создание нового режиссера"""
        req_json = request.json
        director_service.create(req_json)


@director_ns.route('/<int:did>')
class DirectorViews(Resource):

    def get(self, did: int):
        """Получение режиссера по id"""
        director = director_service.get_by_id(did)
        return director_schema.dump(director)

    def put (self, did: int):
        """Обновление данных в режиссере"""
        req_json = request.json
        req_json['id'] = did
        director_service.update(req_json)
        return "Обновленно", 200

    def delete(self, did: int):
        """Удаление режиссера"""
        director_service.delete(did)
        return "Удалено", 200