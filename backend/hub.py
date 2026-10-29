from backend.database import Database
from backend.haiku_service import HaikuService
from backend.user_service import UserService


class Hub:
    def __init__(self):
        database = Database()
        self.user_service = UserService(database)
        self.haiku_service = HaikuService(database)
