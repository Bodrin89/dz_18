from flask import request
from flask_restx import Resource, Namespace

from app.conteiner import genre_service
from app.dao.model.genre import GenreSchema

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genre_ns.route('/')
class GenreViews(Resource):
    def get(self):
        all_genre = genre_service.get_all()
        return genres_schema.dump(all_genre), 200

@genre_ns.route('/<int:gid>')
class GenreViews(Resource):
    def get(self, gid: int):
        genre = genre_service.get_by_id(gid)
        return genre_schema.dump(genre)

