from typing import List
from .settings import Settings


class BulletedList:
    def __init__(
        self,
        data: List[str],
        settings: List[Settings] = None,
        bullet_string: str = "-",
        bullet_settings: Settings = None,
        indent: float = 10,
        between_spacing: float = None
    ):
        """
        Initializes a BulletedList object
        Инициализирует объект BulletedList

        Args:
            data (List[str]):
                A list of strings representing the items of the list
                Список строк, представляющих элементы списка
            settings (List[Settings], optional):
                A list of Settings objects to customize the appearance of each list item. If not specified, default settings are used
                Список объектов Settings для настройки внешнего вида каждого элемента списка. Если не указан, используются настройки по умолчанию
            bullet_string (str, optional):
                The string representing the marker of the list items. Defaults to "-"
                Строка, представляющая маркер элементов списка. По умолчанию "-"
            bullet_settings (Settings, optional):
                A list of Settings objects to customize the appearance of the bullets. If not specified, the default settings are used
                Список объектов Settings для настройки внешнего вида маркировки. Если не указан, используются настройки по умолчанию
            indent (float, optional):
                The indentation of list items from the left edge of the page. Defaults to 10
                Отступ элементов списка от левого края страницы. По умолчанию 10
            between_spacing (float, optional):
                Vertical spacing between list items. If not specified, default settings are used
                Вертикальный интервал между элементами списка. Если не указан, используются настройки по умолчанию
        """
        self.data = data
        if settings is None:
            self.settings = [Settings() for _ in range(len(data))]
        else:
            if len(settings) != len(data):
                raise TypeError("List data and list settings have different shapes.")
            self.settings = settings
        self.bullet_string = bullet_string
        if bullet_settings is None:
            bullet_settings = Settings()
        self.bullet_settings = bullet_settings
        self.indent = indent
        self.between_spacing = between_spacing

    def set_settings(
        self,
        index: int,
        settings: Settings = None
    ) -> None:
        """
        Sets the settings for a specific list item
        Устанавливает настройки для определенного элемента списка

        Args:
            index (int):
                The index of the list item to set settings for (starting from 1)
                Индекс элемента списка, для которого нужно установить настройки (начиная с 1)
            settings (Settings, optional):
                A Settings object with settings for the list item. If not specified, default settings are used
                Объект Settings с настройками для элемента списка. Если не указан, используются настройки по умолчанию
        """
        if settings is None:
            settings = Settings()
        self.settings[index - 1] = settings

    def set_bullet_settings(
        self,
        settings: Settings = None
    ) -> None:
        """
        Sets the settings for the bullets
        Устанавливает настройки для маркировки

        Args:
            settings (Settings, optional):
                A Settings object with settings for the bullets. If not specified, default settings are used
                Объект Settings с настройками для маркировки. Если не указан, используются настройки по умолчанию
        """
        if settings is None:
            settings = Settings()
        self.bullet_settings = settings
