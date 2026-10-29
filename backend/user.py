from typing import NamedTuple

import bcrypt


class User(NamedTuple):
    username: str
    password_hash: str

    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def authenticate(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode(), self.password_hash.encode())
