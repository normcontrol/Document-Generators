class Settings:
    def __init__(
        self,
        font_name: str = None,
        font_size: float = None,
        alignment: str = None,
        bold: bool = None,
        italic: bool = None,
        underline: bool = None
    ):
        """
        Represents settings for text formatting
        Представляет настройки для форматирования текста

        Args:
            font_name (str, optional):
                The name of the font to be used. If not specified, default settings are used
                Имя используемого шрифта. Если не указано, используются настройки по умолчанию
            font_size (float, optional):
                The size of the font. If not specified, default settings are used
                Размер шрифта. Если не указано, используются настройки по умолчанию
            alignment (str, optional):
                The alignment of the text. Can be 'left', 'right', 'center', or 'justify'. If not specified, default settings are used
                Выравнивание текста. Может быть 'left', 'right', 'center' или 'justify'. Если не указано, используются настройки по умолчанию
            bold (bool, optional):
                Whether the text should be bold. If not specified, default settings are used
                Жирный ли текст. Если не указано, используются настройки по умолчанию
            italic (bool, optional):
                Whether the text should be italic. If not specified, default settings are used
                Курсивный ли текст. Если не указано, используются настройки по умолчанию
            underline (bool, optional):
                Whether the text should be underlined. If not specified, default settings are used
                Подчеркнут ли текст. Если не указано, используются настройки по умолчанию
            """
        self.font_name = font_name
        self.font_size = font_size
        self.alignment = alignment
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def get(
        self
    ) -> dict:
        """
        Returns the settings as a dictionary
        Возвращает настройки в виде словаря
        """
        return {
            "font_name": self.font_name,
            "font_size": self.font_size,
            "alignment": self.alignment,
            "bold": self.bold,
            "italic": self.italic,
            "underline": self.underline
        }
