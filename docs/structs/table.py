from typing import List
from .settings import Settings


class Table:
    def __init__(
        self,
        data: List[List[str]],
        settings: List[List[Settings]] = None
    ):
        """
        Initializes an Table object
        Инициализирует объект Table

        Args:
            data (List[List[str]]):
                A 2D list of strings representing the data of the table
                Двумерный список строк, представляющих данные таблицы
            settings (List[List[Settings]], optional):
                A 2D list of Settings objects to customize the appearance of each cell in the table. If not specified, default settings are used
                Двумерный список объектов Settings для настройки внешнего вида каждой ячейки в таблице. Если не указан, используются настройки по умолчанию
        """
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
        """
        Sets the settings for a specific cell in the table
        Устанавливает настройки для определенной ячейки в таблице

        Args:
            row (int):
                The index of the row of the cell (starting from 1)
                Индекс строки ячейки (начиная с 1)
            coll (int):
                The index of the column of the cell (starting from 1)
                Индекс столбца ячейки (начиная с 1)
            settings (Settings, optional):
                A Settings object to customize the appearance of the cell. If not specified, default settings are used
                Объект Settings для настройки внешнего вида ячейки. Если не указан, используются настройки по умолчанию
        """
        if settings is None:
            settings = Settings()
        self.settings[row - 1][coll - 1] = settings
