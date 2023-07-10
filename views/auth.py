from flask import request
from flask_restx import Resource, Namespace

from app.conteiner import auth_service


from app.config import Config
secret = Config.SECRET
algo = Config.ALGO


auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthViews(Resource):
    def post(self):
        data = request.json
        user_name = data.get('username', None)
        password = data.get('password', None)
        role = data.get('role', None)
        if None in [user_name, password]:
            return '', 400
        token = auth_service.generate_token(user_name, password, role)
        return token, 201

    def put(self):
        data = request.json
        token = data.get('refresh_token')
        tokens = auth_service.approve_refresh_token(token)
        return tokens, 201
