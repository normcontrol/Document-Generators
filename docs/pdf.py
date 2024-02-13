from fpdf import FPDF
from fpdf.enums import Align


class PDF:
    def __init__(self) -> None:
        self.__pdf = FPDF()
        self.__font_name = "Arial"
        self.__font_size = 12
        self.__font_styles = {
            "bold": False,
            "italic": False,
            "underline": False
        }
        self.set_font(self.__font_name, self.__font_size, **self.__font_styles)
        self.__line_spacing = 1
        self.__paragraph_spacing = 1

        self.__pdf.add_page()

    def set_font_name(self, name: str) -> None:
        self.__font_name = name
        self.__pdf.set_font(name, self.__pdf.font_style, self.__font_size)

    def set_font_size(self, size: float) -> None:
        self.__font_size = size
        self.__pdf.set_font_size(size)

    def set_font_style(self, bold: bool = None, italic: bool = None, underline: bool = None) -> None:
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

    def set_font(self, name: str = None, size: float = None, bold: bool = None, italic: bool = None, underline: bool = None) -> None:
        if name is not None:
            self.set_font_name(name)
        if size is not None:
            self.set_font_size(size)
        self.set_font_style(bold, italic, underline)

    def set_margin_top(self, top: float) -> None:
        self.__pdf.set_top_margin(top)

    def set_margin_right(self, right: float) -> None:
        self.__pdf.set_right_margin(right)

    def set_margin_bottom(self, bottom: float) -> None:
        self.__pdf.set_auto_page_break(True, bottom)

    def set_margin_left(self, left: float) -> None:
        self.__pdf.set_left_margin(left)

    def set_margin(self, top: float = None, right: float = None, bottom: float = None, left: float = None) -> None:
        if top is not None:
            self.set_margin_top(top)
        if right is not None:
            self.set_margin_right(right)
        if bottom is not None:
            self.set_margin_bottom(bottom)
        if left is not None:
            self.set_margin_left(left)

    def set_line_spacing(self, spacing: float) -> None:
        self.__line_spacing = spacing

    def set_paragraph_spacing(self, spacing: float):
        self.__paragraph_spacing = spacing

    def add_paragraph(self, text: str, alignment: str = "left") -> None:
        align = alignment
        if alignment == "left":
            align = Align.L
        elif alignment == "right":
            align = Align.R
        elif alignment == "center":
            align = Align.C
        elif alignment == "justify":
            align = Align.J
        self.__pdf.set_x(self.__pdf.l_margin)
        if self.__pdf.get_y() < self.__pdf.t_margin:
            self.__pdf.set_y(self.__pdf.t_margin)
        self.__pdf.multi_cell(w=0, h=self.__line_spacing * self.__pdf.font_size, text=text, align=align)
        self.__pdf.set_x(self.__pdf.l_margin)
        self.__pdf.set_y(self.__pdf.get_y() + self.__paragraph_spacing * self.__pdf.font_size)

    def save(self, filename: str) -> None:
        self.__pdf.output(filename)
