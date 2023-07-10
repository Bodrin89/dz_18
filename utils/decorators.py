from flask import request, abort, Flask
from app.config import Config
import jwt

secret = Config.SECRET
algo = Config.ALGO


def auth_required(func):
    """Декоратор права доступа зарегистрированным пользователям"""
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        try:
            jwt.decode(token, secret, algorithms=[algo])
        except Exception as e:
            print("JWT decode Exception", e)
            abort(401)
        return func(*args, **kwargs)
    return wrapper


def admin_required(func):
    """Право доступа администратору"""
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        try:
            data = jwt.decode(token, secret, algorithms=[algo])
        except Exception as e:
            print("JWT decode Exception", e)
            abort(401)

        if not data.get('role').lower() == 'admin':
            abort(401)
        return func(*args, **kwargs)

    return wrapper

