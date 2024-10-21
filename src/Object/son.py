from typing import List


class Son:
    def __init__(self, id_son: int = None, name: str = "", tags: List[str] = None):
        self.id_son = id_son
        self.name = name
        self.tags = tags or []
