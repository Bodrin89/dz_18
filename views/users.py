
from flask import request
from flask_restx import Resource, Namespace

from app.conteiner import user_service
from app.dao.model.users import UserSchema
from utils.decorators import auth_required

user_ns = Namespace('users')
user_schema = UserSchema()


@user_ns.route('/<int:uid>')
class UserViews(Resource):
    """Получить информацию о пользователе"""
    @auth_required
    def get(self, uid: int):
        user = user_service.get_user_id(uid)
        return user_schema.dump(user), 200

    @auth_required
    def patch(self, uid: int):
        """Изменить информацию пользователя (имя, фамилия, любимый жанр)"""
        req_json = request.json
        req_json['id'] = uid
        user = user_service.get_user_id(uid)
        user_service.update_user(req_json, user)
        return '', 201


@user_ns.route('/password/<int:uid>')
class UserViews(Resource):
    @auth_required
    def put(self, uid: int):
        """Обновить пароль пользователя"""
        req_json = request.json
        req_json['id'] = uid
        user = user_service.get_user_id(uid)
        user_service.update_password_user(req_json, user)
        return '', 201

