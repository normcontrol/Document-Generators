from odf.opendocument import OpenDocumentText
from odf.text import P
from odf import teletype
from odf.style import Style, TextProperties, ParagraphProperties, PageLayout, PageLayoutProperties
from .structs import Table, NumberedList, BulletedList, Image, Formula


class ODT:
    def __init__(
        self
    ):
        """
        Initializes a ODT object
        Инициализирует объект ODT
        """
        self.__odt = OpenDocumentText()
        self.__style = Style(name="FOR_ODT", family="paragraph")
        self.__font_name = "Arial"
        self.__font_size = 14
        self.__alignment = "left"
        self.__margin_top = 1
        self.__margin_right = 3
        self.__margin_bottom = 1
        self.__margin_left = 1.25
        self.__font_styles = {
            "bold": False,
            "italic": False,
            "underline": False
        }
        self.__line_spacing = 1
        self.__paragraph_spacing = 1
        self.__first_addition = True
        self.__fixed_paragraph_spacing = None
        self.__increment = 1

    def set_font_name(
        self,
        font_name: str
    ) -> None:
        """
        Sets the font
        Устанавливает шрифт

        Args:
            font_name (str):
                The name of the font to be set
                Имя шрифта, которое нужно установить
        """
        self.__font_name = font_name

    def set_font_size(
        self,
        font_size: float
    ) -> None:
        """
        Sets the font size
        Устанавливает размер шрифта

        Args:
            font_size (float):
                The size of the font to be set
                Размер шрифта, который нужно установить
        """
        self.__font_size = font_size

    def set_alignment(
        self,
        alignment: str
    ) -> None:
        """
        Sets the alignment of the text
        Устанавливает выравнивание текста

        Args:
            alignment (str):
                The alignment of the text. Valid values are 'left', 'right', 'center', 'justify'
                Выравнивание текста. Допустимые значения: 'left', 'right', 'center', 'justify'
        """
        self.__alignment = alignment
        self.__style.addElement(ParagraphProperties(textalign=alignment))

    def set_font_style(
        self,
        bold: bool = None,
        italic: bool = None,
        underline: bool = None
    ) -> None:
        """
        Sets the font style
        Устанавливает стиль шрифта

        Args:
            bold (bool, optional):
                Whether the text should be bold. If not specified, the current bold setting remains unchanged
                Определяет, должен ли текст быть полужирным. Если не указано, текущая настройка полужирного остается без изменений
            italic (bool, optional):
                Whether the text should be italic. If not specified, the current italic setting remains unchanged
                Определяет, должен ли текст быть курсивом. Если не указано, текущая настройка курсива остается без изменений
            underline (bool, optional):
                Whether the text should be underlined. If not specified, the current underline setting remains unchanged
                Определяет, должен ли текст быть подчеркнутым. Если не указано, текущая настройка подчеркивания остается без изменений
        """
        if bold is not None:
            self.__font_styles["bold"] = bold
        if italic is not None:
            self.__font_styles["italic"] = italic
        if underline is not None:
            self.__font_styles["underline"] = underline

    def set_settings(
        self,
        font_name: str = None,
        font_size: float = None,
        alignment: str = None,
        bold: bool = None,
        italic: bool = None,
        underline: bool = None
    ) -> None:
        """
        Sets the settings for document
        Устанавливает настройки для документа

        Args:
            font_name (str, optional):
                The name of the font to be set. If not specified, the current font name remains unchanged
                Имя шрифта, которое нужно установить. Если не указано, текущее имя шрифта остается без изменений
            font_size (float, optional):
                The size of the font to be set. If not specified, the current font size remains unchanged
                Размер шрифта, который нужно установить. Если не указано, текущий размер шрифта остается без изменений
            alignment (str, optional):
                The alignment of the text. Valid values are 'left', 'right', 'center', 'justify'. If not specified, the current alignment remains unchanged
                Выравнивание текста. Допустимые значения: 'left', 'right', 'center', 'justify'. Если не указано, текущее выравнивание остается без изменений
            bold (bool, optional):
                Whether the text should be bold. If not specified, the current bold setting remains unchanged
                Определяет, должен ли текст быть полужирным. Если не указано, текущая настройка полужирного остается без изменений
            italic (bool, optional):
                Whether the text should be italicized. If not specified, the current italic setting remains unchanged
                Определяет, должен ли текст быть курсивом. Если не указано, текущая настройка курсива остается без изменений
            underline (bool, optional):
                Whether the text should be underlined. If not specified, the current underline setting remains unchanged
                Определяет, должен ли текст быть подчеркнутым. Если не указано, текущая настройка подчеркивания остается без изменений
        """
        if font_name is not None:
            self.set_font_name(font_name)
        if font_size is not None:
            self.set_font_size(font_size)
        if alignment is not None:
            self.set_alignment(alignment)
        self.set_font_style(bold, italic, underline)

    def set_margin_top(
        self,
        top: float
    ) -> None:
        """
        Sets the top margin of document
        Устанавливает верхний отступ документа

        Args:
            top (float):
                The value of the top margin to be set
                Значение верхнего поля, которое нужно установить
        """
        self.__margin_top = top

    def set_margin_right(
        self,
        right: float
    ) -> None:
        """
        Sets the right margin of document
        Устанавливает правый отступ документа

        Args:
            right (float):
                The value of the right margin to be set
                Значение правого поля, которое нужно установить
        """
        self.__margin_right = right

    def set_margin_bottom(
        self,
        bottom: float
    ) -> None:
        """
        Sets the bottom margin of document
        Устанавливает нижний отступ документа

        Args:
            bottom (float):
                The value of the bottom margin to be set
                Значение нижнего поля, которое нужно установить
        """
        self.__margin_bottom = bottom

    def set_margin_left(
        self,
        left: float
    ) -> None:
        """
        Sets the left margin of document
        Устанавливает левый отступ документа

        Args:
            left (float):
                The value of the left margin to be set
                Значение левого поля, которое нужно установить
        """
        self.__margin_left = left

    def set_margin(
        self,
        top: float = None,
        right: float = None,
        bottom: float = None,
        left: float = None
    ) -> None:
        """
        Sets the margins of document
        Устанавливает отступы документа

        Args:
            top (float, optional):
                The value of the top margin to be set. If not specified, the top margin remains unchanged
                Значение верхнего поля, которое нужно установить. Если не указано, верхнее поле остается без изменений
            right (float, optional):
                The value of the right margin to be set. If not specified, the right margin remains unchanged
                Значение правого поля, которое нужно установить. Если не указано, правое поле остается без изменений
            bottom (float, optional):
                The value of the bottom margin to be set. If not specified, the bottom margin remains unchanged
                Значение нижнего поля, которое нужно установить. Если не указано, нижнее поле остается без изменений
            left (float, optional):
                The value of the left margin to be set. If not specified, the left margin remains unchanged
                Значение левого поля, которое нужно установить. Если не указано, левое поле остается без изменений
        """
        if top is not None:
            self.set_margin_top(top)
        if right is not None:
            self.set_margin_right(right)
        if bottom is not None:
            self.set_margin_bottom(bottom)
        if left is not None:
            self.set_margin_left(left)

    def set_line_spacing(
        self,
        spacing_k: float = 1
    ) -> None:
        """
        Sets the line spacing of document
        Устанавливает межстрочный интервал документа

        Args:
            spacing_k (float):
                The line spacing factor to be set. Single interval by default
                Фактор межстрочного интервала, который нужно установить. По умолчанию одинарный интервал
        """
        self.__line_spacing = spacing_k

    def set_paragraph_spacing(
        self,
        spacing_k: float = 1
    ) -> None:
        """
        Sets the paragraph spacing of document
        Устанавливает интервал между абзацами документа

        Args:
            spacing_k (float):
                The paragraph spacing factor to be set. Single interval by default
                Фактор интервала между абзацами, который нужно установить. По умолчанию одинарный интервал
        """
        self.__paragraph_spacing = spacing_k

    def set_fixed_paragraph_spacing(
        self,
        spacing: float = None
    ) -> None:
        """
        Sets the fixed paragraph spacing of document
        Фиксирует интервал между абзацами документа

        Args:
            spacing (float, optional):
                The fixed spacing value to be set. If not specified, removes the fixed interval
                Значение фиксированного интервала, которое нужно установить. Если не указано, убирает фиксированный интервал
        """
        if spacing is not None:
            self.__fixed_paragraph_spacing = spacing
        else:
            self.__fixed_paragraph_spacing = None

    def add_paragraph(
        self,
        text: str,
        spacing: float = None,
        font_name: str = None,
        font_size: float = None,
        alignment: str = None,
        bold: bool = None,
        italic: bool = None,
        underline: bool = None
    ) -> None:
        style = Style(name=f"ODT_{self.__increment}", family="paragraph")
        self.__increment += 1
        if spacing:
            space = spacing
        elif self.__fixed_paragraph_spacing:
            space = self.__fixed_paragraph_spacing
        else:
            space = self.__paragraph_spacing * font_size
        style.addElement(ParagraphProperties(
            textalign=alignment or self.__alignment,
            margintop=f"{space}cm",
            marginright=f"{self.__margin_right - 1.5}cm",
            marginleft=f"{self.__margin_left - 3}cm"
        ))
        style.addElement(TextProperties(
            fontfamily=font_name or self.__font_name,
            fontsize=f"{font_size or self.__font_size}pt",
            fontweight="bold" if bold or bold is None and self.__font_styles["bold"] else "normal",
            fontstyle="italic" if italic or italic is None and self.__font_styles["italic"] else "normal",
            textunderlinestyle="solid" if underline or underline is None and self.__font_styles["italic"] else "normal",
        ))
        element = P(stylename=style)
        self.__odt.styles.addElement(style)
        teletype.addTextToElement(element, text)
        self.__odt.text.addElement(element)

    def save(
        self,
        file_path: str
    ) -> None:
        """
        Saves document to a file
        Сохраняет документ в файл

        Args:
            file_path (str):
                The path to the file to save
                Путь к файлу для сохранения
        """
        self.__odt.save(file_path)
