
class Config:
    DEBUG =True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 4}
    SECRET = 'Sq$wW'
    ALGO = 'HS256'
    POSTS_OF_PAGE = 12


