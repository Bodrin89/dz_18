
from app.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
import hashlib
import base64
import hmac

from app.dao.users import UserDAO

class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_by_name(self, user_name):
        """Получение юзера по имени и паролю"""
        return self.dao.get_by_name(user_name)

    def create_user(self, user_data):
        """Создание юзера"""
        user_data['password'] = self.generate_password(user_data['password'])
        return self.dao.create(user_data)

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
