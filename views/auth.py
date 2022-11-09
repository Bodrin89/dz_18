from flask import request
from flask_restx import Resource, Namespace

from app.conteiner import auth_service


from app.config import Config
secret = Config.SECRET
algo = Config.ALGO


auth_ns = Namespace('auth')


@auth_ns.route('/register')
class AuthViews(Resource):
    """Создание юзера"""
    def post(self):
        req_json = request.json
        auth_service.create_user(req_json)
        return 201


@auth_ns.route('/login')
class AuthViews(Resource):
    """Аутентификация пользователя"""
    def post(self):
        data = request.json
        password = data.get('password', None)
        email = data.get('email', None)
        if None in [email, password]:
            return '', 400
        token = auth_service.generate_token(password, email)
        return token, 201

    def put(self):
        """Обновление токенов"""
        data = request.json
        token = data.get('refresh_token')
        tokens = auth_service.approve_refresh_token(token)
        return tokens, 201


