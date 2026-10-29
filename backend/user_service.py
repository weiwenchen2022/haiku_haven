from typing import Optional

from backend.database import Database
from backend.user import User


class UserService:
    def __init__(self, database: Database) -> None:
        self.database = database

    def get_user(self, username) -> Optional[User]:
        query = """
            SELECT username, password_hash
            FROM users
            WHERE username = :username
        """
        params = dict(username=username)
        results = self.database.execute_query(query, params)
        return User(*results[0]) if results else None

    def create_user(self, username: str, password: str) -> Optional[User]:
        existing_user = self.get_user(username)
        if existing_user:
            return None

        query = """
            INSERT INTO users (username, password_hash)
            VALUES (:username, :password_hash)
            RETURNING username, password_hash
        """

        password_hash = User.hash_password(password)
        params = dict(username=username, password_hash=password_hash)
        results = self.database.execute_query(query, params, write=True)
        return User(*results[0]) if results else None

    def get_authenticated_user(
        self,
        username: str,
        password: str,
    ) -> Optional[User]:
        user = self.get_user(username)
        if user and user.authenticate(password):
            return user
        return None
