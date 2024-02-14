from .settings import Settings


class Image:
    def __init__(
        self,
        image_path: str,
        settings: Settings = None
    ):
        self.image_path = image_path
        if settings is None:
            self.settings = Settings()
        else:
            self.settings = settings

    def set_settings(
        self,
        settings: Settings = None
    ) -> None:
        if settings is None:
            settings = Settings()
        self.settings = settings
