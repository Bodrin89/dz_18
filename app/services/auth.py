from flask import request, abort, Flask
from app.config import Config
from app.services.user import UserService
import calendar
import datetime
import jwt

secret = Config.SECRET
algo = Config.ALGO


class AuthService():
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_token(self, user_name, password, role, is_refresh=False):
        """Создание токенов"""
        user = self.user_service.get_by_name(user_name)
        if user is None:
            raise abort(404)
        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                raise abort(400)


        """Создание токена с временем действия 30 минут"""
        data = {'username': user_name, 'password': password, 'role': role}
        min_30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min_30.timetuple())
        access_token = jwt.encode(data, secret, algorithm=algo)

        """Создание токена с временем действия 130 дней"""
        data = {'username': user_name, 'password': password, 'role': role}
        days_130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days_130.timetuple())
        refresh_token = jwt.encode(data, secret, algorithm=algo)
        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=secret, algorithms=[algo])
        username = data.get('username')
        return self.generate_token(username, None, None, is_refresh=True)




