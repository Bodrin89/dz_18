
from flask import request
from flask_restx import Resource, Namespace

from app.conteiner import user_service
from app.dao.model.users import UserSchema
from utils.decorators import auth_required
from utils.funcs import generate_password

user_ns = Namespace('users')
user_schema = UserSchema()


@user_ns.route('/')
class UserViews(Resource):
    """Получить информацию о пользователе"""
    @auth_required
    def get(self, data=None):
        hash_password = generate_password(data["password"])
        user = user_service.get_user(hash_password, data["email"])
        return user_schema.dump(user), 200

    @auth_required
    def patch(self, data=None):
        """Изменить информацию пользователя (имя, фамилия, любимый жанр)"""
        hash_password = generate_password(data["password"])
        user = user_service.get_user(hash_password, data["email"])
        req_json = request.json
        req_json["id"] = user.id
        user_service.update_user(req_json, user)
        return '', 201


@user_ns.route('/password')
class UserViews(Resource):
    @auth_required
    def put(self, data=None):
        """Обновить пароль пользователя"""
        hash_password = generate_password(data["password"])
        user = user_service.get_user(hash_password, data["email"])
        req_json = request.json
        req_json['id'] = user.id
        user_service.update_password_user(req_json, user)
        return '', 201

