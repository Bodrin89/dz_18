
from app.dao.director import DirectorDAO

class DirectorService():
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, did):
        return self.dao.get_by_id(did)