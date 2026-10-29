from collections.abc import Sequence
from typing import Optional

from backend.database import Database
from backend.haiku import Haiku


class HaikuService:
    def __init__(self, database: Database) -> None:
        self.database = database

    def create_haiku(self, author: str, haiku_text: str) -> Optional[Haiku]:
        query = """
            INSERT INTO haikus (author, text)
            VALUES (:author, :text)
            RETURNING haiku_id, created_at, author, text
        """
        params = dict(author=author, text=haiku_text)
        results = self.database.execute_query(query, params, write=True)
        return Haiku(*results[0]) if results else None

    def get_haikus_by_author(self, author: str) -> Sequence[Haiku]:
        query = """
            SELECT *
            FROM haikus
            WHERE author = :author
        """
        params = dict(author=author)
        results = self.database.execute_query(query, params)
        return [Haiku(*row) for row in results]

    def update_haiku(self, haiku_id: int, haiku_text: str) -> Optional[Haiku]:
        query = """
            UPDATE haikus
            SET text = :text
            WHERE haiku_id = :id
            RETURNING *
        """
        params = dict(text=haiku_text, id=haiku_id)
        results = self.database.execute_query(query, params, write=True)
        return Haiku(*results[0]) if results else None

    def delete_haiku(self, haiku_id: int) -> Optional[Haiku]:
        query = """
            DELETE FROM haikus
            WHERE haiku_id = :id
            RETURNING *
        """
        params = dict(id=haiku_id)
        results = self.database.execute_query(query, params, write=True)
        return Haiku(*results[0]) if results else None
