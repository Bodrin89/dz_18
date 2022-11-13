from flask import request, abort
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
        data = jwt.decode(token, secret, algorithms=[algo])
        try:
            jwt.decode(token, secret, algorithms=[algo])
        except Exception as e:
            print("JWT decode Exception", e)
            abort(401)
        return func(data=data, *args, **kwargs)
    return wrapper


