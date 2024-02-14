from fpdf import FPDF
from fpdf.enums import Align
from fpdf.fonts import FontFace
from .structs import Table, NumberedList, BulletedList


class PDF:
    def __init__(
        self
    ):
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
        self.__pdf.add_page()

    def add_font(
        self,
        font_path: str
    ) -> None:
        self.__pdf.add_font(fname=font_path)

    def set_font_name(
        self,
        font_name: str
    ) -> None:
        self.__font_name = font_name
        self.__pdf.set_font(font_name, self.__pdf.font_style, self.__font_size)

    def set_font_size(
        self,
        font_size: float
    ) -> None:
        self.__font_size = font_size
        self.__pdf.set_font_size(font_size)

    def set_alignment(
        self,
        alignment: str
    ) -> None:
        self._make_alignment(alignment)
        self.__alignment = alignment

    def set_font_style(
        self,
        bold: bool = None,
        italic: bool = None,
        underline: bool = None
    ) -> None:
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
        self.__pdf.set_top_margin(top)

    def set_margin_right(
        self,
        right: float
    ) -> None:
        self.__pdf.set_right_margin(right)

    def set_margin_bottom(
        self,
        bottom: float
    ) -> None:
        self.__pdf.set_auto_page_break(True, bottom)

    def set_margin_left(
        self,
        left: float
    ) -> None:
        self.__pdf.set_left_margin(left)

    def set_margin(
        self,
        top: float = None,
        right: float = None,
        bottom: float = None,
        left: float = None
    ) -> None:
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
        spacing_k: float
    ) -> None:
        self.__line_spacing = spacing_k

    def set_paragraph_spacing(
        self,
        spacing_k: float
    ) -> None:
        self.__paragraph_spacing = spacing_k

    def set_fixed_paragraph_spacing(
        self,
        spacing: float = None
    ) -> None:
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
        last_font_name = self.__font_name
        last_font_size = self.__font_size
        last_alignment = self.__alignment
        last_font_styles = self.__font_styles.copy()
        self.add_spacing(spacing)
        self.set_settings(font_name, font_size, alignment, bold, italic, underline)
        self.__pdf.multi_cell(w=0, text=text, align=self._make_alignment(self.__alignment))
        self.set_settings(last_font_name, last_font_size, last_alignment, **last_font_styles)

    def add_numbered_list(
        self,
        numbered_list: NumberedList,
        spacing: float = None
    ):
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
            self.add_spacing(up_spacing)
            last_font_name = self.__font_name
            last_font_size = self.__font_size
            last_alignment = self.__alignment
            last_font_styles = self.__font_styles.copy()
            settings = numbered_list.settings[i]
            self.set_settings(**settings.get())
            if settings.alignment is None:
                align = self.__alignment
            else:
                align = settings.alignment
            self.__pdf.cell(text=index, align=self._make_alignment(align))
            self.__pdf.multi_cell(w=0, text=text, align=self._make_alignment(align))
            self.set_settings(last_font_name, last_font_size, last_alignment, **last_font_styles)

    def add_bulleted_list(
        self,
        bulleted_list: BulletedList,
        spacing: float = None
    ):
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
            self.add_spacing(up_spacing)
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
            self.__pdf.cell(text=index, align=self._make_alignment(align))
            self.__pdf.multi_cell(w=0, text=text, align=self._make_alignment(align))
            self.set_settings(last_font_name, last_font_size, last_alignment, **last_font_styles)

    def add_image(
        self,
        image_path: str,
        image_width: float = None,
        image_height: float = None,
        image_alignment: str = None,
        text: str = None,
        spacing: float = None,
        font_name: str = None,
        font_size: float = None,
        alignment: str = None,
        bold: bool = None,
        italic: bool = None,
        underline: bool = None
    ) -> None:
        width = 0 if image_width is None else image_width
        height = 0 if image_height is None else image_height
        img_alignment = self.__alignment if image_alignment is None else image_alignment
        self.add_spacing()
        self.__pdf.image(image_path, x=self._make_alignment(img_alignment), w=width, h=height)
        if text is not None:
            self.add_paragraph(
                text,
                spacing,
                font_name,
                font_size,
                alignment,
                bold,
                italic,
                underline
            )

    def add_table(
        self,
        table: Table,
        spacing: float = None
    ) -> None:
        self.add_spacing(spacing)
        with self.__pdf.table(first_row_as_headings=False) as t:
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

    def add_spacing(
        self,
        spacing: float = None
    ) -> None:
        self.__pdf.set_x(self.__pdf.l_margin)
        if spacing is not None:
            self.__pdf.set_y(self.__pdf.get_y() + spacing)
        elif self.__fixed_paragraph_spacing is not None:
            self.__pdf.set_y(self.__pdf.get_y() + self.__fixed_paragraph_spacing)
        else:
            self.__pdf.set_y(self.__pdf.get_y() + self.__paragraph_spacing * self.__pdf.font_size)
        if self.__first_addition:
            self.__first_addition = False
            self.__pdf.set_y(self.__pdf.t_margin)

    def save(
        self,
        filename: str
    ) -> None:
        self.__pdf.output(filename)

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
