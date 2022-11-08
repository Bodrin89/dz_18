
from app.config import Config


def pagination():
    """ Функция разбиения данных на страницы"""
    posts = Config.POSTS_OF_PAGE  # Количество записей на странице
    dict_pages = {x: x + posts for x in range(10000)[::12]}  # Разбиение на страницы по кол-ву записей
    list_pages = []
    for i in dict_pages.items():
        list_pages.append(i)
    return list_pages

def check_email(array_email):
    """Проверка совпадения email в БД"""
    list_email = []
    for i in array_email:
        for item in i:
            list_email.append(item)
    return list_email


