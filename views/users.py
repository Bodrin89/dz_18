
from flask import request
from flask_restx import Resource, Namespace

from app.conteiner import user_service
from app.dao.model.users import UserSchema
from utils.decorators import auth_required

user_ns = Namespace('users')
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_ns.route('/')
class UserViews(Resource):
    @auth_required
    def post(self):
        req_json = request.json
        user_service.create_user(req_json)
        return 201


@user_ns.route('/<int:uid>')
class UserViews(Resource):
    @auth_required
    def get(self, uid: int):
        user = user_service.get_user_id(uid)
        return user_schema.dump(user)

    @auth_required
    def patch(self, uid: int):
        req_json = request.json
        req_json['id'] = uid
        user = user_service.get_user_id(uid)
        user_service.update_user(req_json, user)
        return '', 200

