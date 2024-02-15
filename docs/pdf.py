from fpdf import FPDF
from fpdf.enums import Align
from fpdf.fonts import FontFace
from io import BytesIO
from urllib.parse import quote
from urllib.request import urlopen
from matplotlib.figure import Figure
from .structs import Table, NumberedList, BulletedList, Image


class PDF:
    def __init__(
        self
    ):
        """
        Initializes a PDF object
        Инициализирует объект PDF
        """
        self.__pdf = FPDF()
        self.__font_name = "Arial"
        self.__font_size = 14
        self.__alignment = "left"
        self.__font_styles = {
            "bold": False,
            "italic": False,
            "underline": False
        }
        self.set_settings(self.__font_name, self.__font_size, self.__alignment, **self.__font_styles)
        self.__line_spacing = 1
        self.__paragraph_spacing = 1
        self.__first_addition = True
        self.__fixed_paragraph_spacing = None
        self.__cm_k = 10
        self.__pdf.add_page()

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
        self.__pdf.set_font(font_name, self.__pdf.font_style, self.__font_size)

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
        self.__pdf.set_font_size(font_size)

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
        self._make_alignment(alignment)
        self.__alignment = alignment

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
        style = ""
        for type in self.__font_styles:
            if self.__font_styles[type]:
                style += type[0].upper()
        self.__pdf.set_font(self.__font_name, style, self.__font_size)

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
        self.__pdf.set_top_margin(top * self.__cm_k)

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
        self.__pdf.set_right_margin(right * self.__cm_k)

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
        self.__pdf.set_auto_page_break(True, bottom * self.__cm_k)

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
        self.__pdf.set_left_margin(left * self.__cm_k)

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
        """
        Adds a paragraph to document
        Добавляет параграф в документ

        Args:
            text (str):
                The text content of the paragraph
                Текстовое содержимое абзаца
            spacing (float, optional):
                The spacing to be added before the paragraph. If not specified, default settings are used
                Интервал, добавляемый перед абзацем. Если не указан, используются настройки по умолчанию
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
        last_font_name = self.__font_name
        last_font_size = self.__font_size
        last_alignment = self.__alignment
        last_font_styles = self.__font_styles.copy()
        self._add_spacing(spacing)
        self.set_settings(font_name, font_size, alignment, bold, italic, underline)
        self.__pdf.multi_cell(w=0, text=text, align=self._make_alignment(self.__alignment))
        self.set_settings(last_font_name, last_font_size, last_alignment, **last_font_styles)

    def add_numbered_list(
        self,
        numbered_list: NumberedList,
        spacing: float = None
    ) -> None:
        """
        Adds a numbered list to document
        Добавляет нумерованный список в документ

        Args:
            numbered_list (NumberedList):
                The list object to be added
                Объект списка, который нужно добавить
            spacing (float, optional):
                The interval to add before the start of the list. If not specified, the default settings are used
                Интервал, добавляемый перед началом списка. Если не указан, используются настройки по умолчанию
        """
        for i in range(len(numbered_list.data)):
            if i == 0:
                if spacing is not None:
                    up_spacing = spacing
                elif self.__fixed_paragraph_spacing is not None:
                    up_spacing = self.__fixed_paragraph_spacing
                else:
                    up_spacing = self.__paragraph_spacing
            else:
                up_spacing = numbered_list.between_spacing
            index = numbered_list.number_string.replace("{i}", str(numbered_list.number_start + i * numbered_list.number_increment)) + " "
            text = numbered_list.data[i]
            self._add_spacing(up_spacing)
            last_font_name = self.__font_name
            last_font_size = self.__font_size
            last_alignment = self.__alignment
            last_font_styles = self.__font_styles.copy()
            settings = numbered_list.settings[i]
            if settings.alignment is None:
                align = self.__alignment
            else:
                align = settings.alignment
            self.__pdf.set_x(self.__pdf.get_x() + numbered_list.indent * self.__cm_k)
            self.set_settings(**numbered_list.number_settings.get())
            self.__pdf.cell(text=index, align=self._make_alignment(align))
            self.set_settings(last_font_name, last_font_size, last_alignment, **last_font_styles)
            self.set_settings(**settings.get())
            self.__pdf.multi_cell(w=0, text=text, align=self._make_alignment(align))
            self.set_settings(last_font_name, last_font_size, last_alignment, **last_font_styles)

    def add_bulleted_list(
        self,
        bulleted_list: BulletedList,
        spacing: float = None
    ) -> None:
        """
        Adds a bulleted list to document
        Добавляет маркированный список в документ

        Args:
            bulleted_list (BulletedList):
                The list object to be added
                Объект списка, который нужно добавить
            spacing (float, optional):
                The interval to add before the start of the list. If not specified, the default settings are used
                Интервал, добавляемый перед началом списка. Если не указан, используются настройки по умолчанию
        """
        for i in range(len(bulleted_list.data)):
            if i == 0:
                if spacing is not None:
                    up_spacing = spacing
                elif self.__fixed_paragraph_spacing is not None:
                    up_spacing = self.__fixed_paragraph_spacing
                else:
                    up_spacing = self.__paragraph_spacing
            else:
                up_spacing = bulleted_list.between_spacing
            index = bulleted_list.bullet_string + " "
            text = bulleted_list.data[i]
            self._add_spacing(up_spacing)
            last_font_name = self.__font_name
            last_font_size = self.__font_size
            last_alignment = self.__alignment
            last_font_styles = self.__font_styles.copy()
            settings = bulleted_list.settings[i]
            self.set_settings(**settings.get())
            if settings.alignment is None:
                align = self.__alignment
            else:
                align = settings.alignment
            self.__pdf.set_x(self.__pdf.get_x() + bulleted_list.indent * self.__cm_k)
            self.set_settings(**bulleted_list.bullet_settings.get())
            self.__pdf.cell(text=index, align=self._make_alignment(align))
            self.set_settings(last_font_name, last_font_size, last_alignment, **last_font_styles)
            self.set_settings(**settings.get())
            self.__pdf.multi_cell(w=0, text=text, align=self._make_alignment(align))
            self.set_settings(last_font_name, last_font_size, last_alignment, **last_font_styles)

    def add_image(
        self,
        image: Image,
        image_width: float,
        image_height: float,
        image_alignment: str = None,
        image_spacing: float = None,
        caption: str = None,
        caption_spacing: float = None
    ) -> None:
        """
        Adds an image to document
        Добавляет изображение в документ

        Args:
            image (Image):
                The image object to be added
                Объект изображения, который нужно добавить
            image_width (float):
                The width of the image in document
                Ширина изображения в документе
            image_height (float):
                The height of the image in document
                Высота изображения в документе
            image_alignment (str, optional):
                The alignment of the image. Can be 'left', 'right', 'center', or 'justify'. If not specified, default settings are used
                Выравнивание изображения. Может быть 'left', 'right', 'center' или 'justify'. Если не указано, используются настройки по умолчанию
            image_spacing (float, optional):
                The spacing to be added before the image. If not specified, the default settings are used
                Интервал, добавляемый перед изображением. Если не указан, используются настройки по умолчанию
            caption (str, optional):
                The text to be added below the image. If not specified, the text is not added
                Текст, который нужно добавить под изображением. Если не указан, текст не добавляется
            caption_spacing (float, optional):
                The spacing to be added before the text. If not specified, the default settings are used
                Интервал, добавляемый перед текстом. Если не указан, используются настройки по умолчанию
        """
        settings = image.settings
        img_alignment = self.__alignment if image_alignment is None else image_alignment
        self._add_spacing(image_spacing)
        self.__pdf.image(image.image_path, x=self._make_alignment(img_alignment), w=image_width * self.__cm_k, h=image_height * self.__cm_k)
        if caption is not None:
            self.add_paragraph(caption, caption_spacing, **settings.get())

    def add_table(
        self,
        table: Table,
        table_width: float,
        table_height: float,
        table_alignment: str = None,
        spacing: float = None
    ) -> None:
        """
        Adds a table to document
        Добавляет таблицу в документ

        Args:
            table (Table):
                The table object to be added
                Объект таблицы, который нужно добавить
            table_width (float)
                The width of the table in document
                Ширина таблицы в документе
            table_height (float)
                The height of the table in document
                Высота таблицы в документе
            table_alignment (str, optional)
                The alignment of the table. Can be 'left', 'right', 'center', or 'justify'. If not specified, default settings are used
                Выравнивание таблицы. Может быть 'left', 'right', 'center' или 'justify'. Если не указано, используются настройки по умолчанию
            spacing (float, optional):
                The spacing to be added before the table. If not specified, the default settings are used
                Интервал, добавляемый перед таблицей. Если не указан, используются настройки по умолчанию
        """
        self._add_spacing(spacing)
        with self.__pdf.table(
            first_row_as_headings=False,
            align=self._make_alignment(table_alignment or self.__alignment),
            width=table_width * self.__cm_k
        ) as t:
            for i in range(len(table.data)):
                row = t.row()
                for j in range(len(table.data[i])):
                    params = table.settings[i][j]
                    style = ""
                    if params.bold or params.bold is None and self.__font_styles["bold"]:
                        style += "B"
                    if params.italic or params.italic is None and self.__font_styles["italic"]:
                        style += "I"
                    if params.underline or params.underline is None and self.__font_styles["underline"]:
                        style += "U"
                    row.cell(table.data[i][j], style=FontFace(emphasis=style), align=self._make_alignment(params.alignment or self.__alignment))

    def add_formula(
        self,
        formula: str,
        formula_width: float,
        formula_height: float,
        formula_alignment: str = None,
        spacing: float = None
    ) -> None:
        """
        Adds a formula to document
        Добавляет формулу в документ

        Args:
            formula (str):
                The formula string to be added
                Строка формулы, которую нужно добавить
            formula_width (float)
                The width of the formula in document
                Ширина формулы в документе
            formula_height (float)
                The height of the formula in document
                Высота формулы в документе
            formula_alignment (str, optional)
                The alignment of the formula. Can be 'left', 'right', 'center', or 'justify'. If not specified, default settings are used
                Выравнивание формулы. Может быть 'left', 'right', 'center' или 'justify'. Если не указано, используются настройки по умолчанию
            spacing (float, optional):
                The spacing to be added before the formula. If not specified, the default settings are used
                Интервал, добавляемый перед формулой. Если не указан, используются настройки по умолчанию
        """
        self._add_spacing(spacing)
        url = f"https://chart.googleapis.com/chart?cht=tx&chs=512&chl={quote(formula)}"
        with urlopen(url) as img_file:
            img = BytesIO(img_file.read())
        self.__pdf.image(img, x=self._make_alignment(formula_alignment), w=formula_width * self.__cm_k, h=formula_height * self.__cm_k)

    def _add_spacing(
        self,
        spacing: float = None
    ) -> None:
        """
        Adds spacing to document
        Добавляет интервал в документ

        Args:
            spacing (float, optional):
                The interval to be added. If not specified, the default settings are used
                Добавляемый интервал. Если не указан, используются настройки по умолчанию
        """
        self.__pdf.set_x(self.__pdf.l_margin)
        if spacing is not None:
            self.__pdf.set_y(self.__pdf.get_y() + spacing * self.__cm_k)
        elif self.__fixed_paragraph_spacing is not None:
            self.__pdf.set_y(self.__pdf.get_y() + self.__fixed_paragraph_spacing * self.__cm_k)
        else:
            self.__pdf.set_y(self.__pdf.get_y() + self.__paragraph_spacing * self.__pdf.font_size * self.__cm_k)
        if self.__first_addition:
            self.__first_addition = False
            self.__pdf.set_y(self.__pdf.t_margin)

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
        self.__pdf.output(file_path)

    @staticmethod
    def _make_alignment(
        alignment: str
    ) -> Align:
        if alignment == "left":
            return Align.L
        elif alignment == "right":
            return Align.R
        elif alignment == "center":
            return Align.C
        elif alignment == "justify":
            return Align.J
        raise TypeError(f"Alignment '{alignment}' is not valid. Valid values are 'left', 'right', 'center', 'justify'.")
