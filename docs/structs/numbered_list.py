from typing import List
from .settings import Settings


class NumberedList:
    def __init__(
        self,
        data: List[str],
        settings: List[Settings] = None,
        number_start: int = 1,
        number_increment: int = 1,
        number_string: str = "{i}.",
        indent: float = 10,
        between_spacing: float = None
    ):
        self.data = data
        if settings is None:
            self.settings = [Settings() for _ in range(len(data))]
        else:
            if len(settings) != len(data):
                raise TypeError("List data and list settings have different shapes.")
            self.settings = settings
        self.number_start = number_start
        self.number_increment = number_increment
        self.number_string = number_string
        self.indent = indent
        self.between_spacing = between_spacing

    def set_settings(
        self,
        index: int,
        settings: Settings = None
    ) -> None:
        if settings is None:
            settings = Settings()
        self.settings[index - 1] = settings
