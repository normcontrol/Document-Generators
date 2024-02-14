from typing import List
from .settings import Settings


class Table:
    def __init__(
        self,
        data: List[List[str]],
        settings: List[List[Settings]] = None
    ):
        self.data = data
        if len(set([len(row) for row in data])) != 1:
            raise TypeError("Table data has different length of rows.")
        if settings is None:
            self.settings = [[Settings() for _ in range(len(data[0]))] for _ in range(len(data))]
        else:
            if len(set([len(row) for row in settings])) != 1:
                raise TypeError("Table settings has different length of rows.")
            if len(settings[0]) != len(data[0]) or len(settings) != len(data):
                raise TypeError("Table data and table settings have different shapes.")
            self.settings = settings

    def set_settings(
        self,
        row: int,
        coll: int,
        settings: Settings = None
    ) -> None:
        if settings is None:
            settings = Settings()
        self.settings[row - 1][coll - 1] = settings
