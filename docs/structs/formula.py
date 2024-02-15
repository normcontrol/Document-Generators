from .settings import Settings


class Formula:
    def __init__(
        self,
        formula: str,
        settings: Settings = None
    ):
        """
        Initializes an Image object
        Инициализирует объект Image

        Args:
            formula (str):
                The formula string
                Строка формулы
            settings (Settings, optional):
                A Settings object to customize the appearance of the formula. If not specified, default settings are used
                Объект Settings для настройки внешнего вида формулы. Если не указан, используются настройки по умолчанию
        """
        self.formula = formula
        if settings is None:
            settings = Settings()
        self.settings = settings

    def set_settings(
        self,
        settings: Settings = None
    ) -> None:
        """
        Sets the settings for the formula
        Устанавливает настройки для формулы

        Args:
            settings (Settings, optional):
                A Settings object to customize the appearance of the formula. If not specified, default settings are used
                Объект Settings для настройки внешнего вида формулы. Если не указан, используются настройки по умолчанию
        """
        if settings is None:
            settings = Settings()
        self.settings = settings
