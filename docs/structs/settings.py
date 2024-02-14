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
        self.font_name = font_name
        self.font_size = font_size
        self.alignment = alignment
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def get(
        self
    ) -> dict:
        return {
            "font_name": self.font_name,
            "font_size": self.font_size,
            "alignment": self.alignment,
            "bold": self.bold,
            "italic": self.italic,
            "underline": self.underline
        }
