from datetime import datetime
from typing import NamedTuple


class Haiku(NamedTuple):
    haiku_id: int
    created_at: datetime
    author: str
    text: str
