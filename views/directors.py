
from flask import request
from flask_restx import Resource, Namespace

from app.conteiner import director_service
from app.dao.model.director import DirectorSchema

director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@director_ns.route('/')
class DirectorViews(Resource):
    def get(self):
        all_director = director_service.get_all()
        return directors_schema.dump(all_director), 200

@director_ns.route('/<int:did>')
class DirectorViews(Resource):
    def get(self, did: int):
        director = director_service.get_by_id(did)
        return director_schema.dump(director)