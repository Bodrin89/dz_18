import base64
import hashlib
import hmac

from flask import request, abort, Flask
from app.config import Config
from app.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from app.dao.auth import AuthDAO
from app.services.user import UserService
import calendar
import datetime
import jwt

secret = Config.SECRET
algo = Config.ALGO


class AuthService:
    def __init__(self,  user_service: UserService, dao: AuthDAO):
        self.dao = dao
        self.user_service = user_service

    def create_user(self, user_data):
        """Создание юзера"""
        user_data['password'] = self.generate_password(user_data['password'])
        return self.dao.create(user_data)

    def generate_token(self, password, email, is_refresh=False):
        password_hash = self.generate_password(password)
        """Создание токенов"""
        user = self.user_service.get_user(password_hash, email)
        if user is None:
            raise abort(404)
        if not is_refresh:
            if not self.compare_passwords(user.password, password):
                raise abort(400)

        """Создание токена с временем действия 30 минут"""
        data = {'password': password, 'email': email}
        min_30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min_30.timetuple())
        access_token = jwt.encode(data, secret, algorithm=algo)

        """Создание токена с временем действия 130 дней"""
        data = {'password': password, 'email': email}
        days_130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days_130.timetuple())
        refresh_token = jwt.encode(data, secret, algorithm=algo)
        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def approve_refresh_token(self, refresh_token):

        data = jwt.decode(jwt=refresh_token, key=secret, algorithms=[algo])
        password = data.get('password')
        email = data.get("email")
        return self.generate_token(password, email, is_refresh=True)


    def generate_password(self, password):
        """ Создание хэша пароля"""
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def compare_passwords(self, password_hash, other_password) -> bool:
        decoded_digest = base64.b64decode(password_hash)
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode(),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return hmac.compare_digest(decoded_digest, hash_digest)




