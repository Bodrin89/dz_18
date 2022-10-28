
from flask import request
from flask_restx import Resource, Namespace

from app.conteiner import user_service
from app.dao.model.users import UserSchema

user_ns = Namespace('users')
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_ns.route('/')
class UserViews(Resource):
    def post(self):
        req_json = request.json
        user_service.create_user(req_json)
        return 'Создано', 201


@user_ns.route('/<user_name>')
class UserViews(Resource):
    def get(self, user_name):
        user = user_service.get_by_name(user_name)
        return user_schema.dump(user)

