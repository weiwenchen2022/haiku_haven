import streamlit as st
from sqlalchemy import text


class Database:
    def __init__(self) -> None:
        self.conn = st.connection("haikuconn", type="sql")

    def execute_query(
        self,
        query: str,
        params: dict = {},
        write: bool = False,
    ):
        with self.conn.session as session:
            try:
                result = session.execute(text(query), params)
            except Exception:
                if write:
                    session.rollback()

                raise
            else:
                if write:
                    session.commit()

                return result.fetchall()
