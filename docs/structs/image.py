from .settings import Settings


class Image:
    def __init__(
        self,
        image_path: str,
        settings: Settings = None
    ):
        """
        Initializes an Image object
        Инициализирует объект Image

        Args:
            image_path (str):
                The file path to the image file (system or URL)
                Путь к файлу изображения (системный или URL)
            settings (Settings, optional):
                A Settings object to customize the appearance of the image. If not specified, default settings are used
                Объект Settings для настройки внешнего вида изображения. Если не указан, используются настройки по умолчанию
        """
        self.image_path = image_path
        if settings is None:
            settings = Settings()
        self.settings = settings

    def set_settings(
        self,
        settings: Settings = None
    ) -> None:
        """
        Sets the settings for the caption of image
        Устанавливает настройки для подписи изображения

        Args:
            settings (Settings, optional):
                A Settings object to customize the appearance of the caption. If not specified, default settings are used
                Объект Settings для настройки внешнего вида подписи. Если не указан, используются настройки по умолчанию
        """
        if settings is None:
            settings = Settings()
        self.settings = settings
