from fpdf import FPDF
from fpdf.enums import XPos, YPos


class PDF:
    def __init__(self):
        self.__pdf = FPDF()
        self.__paragraph_spacing = 10
        self.__font_name = "Arial"
        self.__font_size = 10
        self.__font_styles = {
            "bold": False,
            "italic": False,
            "underline": False
        }
        self.set_font(self.__font_name, self.__font_size, **self.__font_styles)
        self.__pdf.add_page()

    def set_font_name(self, name):
        self.__font_name = name
        self.__pdf.set_font(name, self.__pdf.font_style, self.__font_size)

    def set_font_size(self, size):
        self.__font_size = size
        self.__pdf.set_font_size(size)

    def set_font_style(self, bold=None, italic=None, underline=None):
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

    def set_font(self, name=None, size=None, bold=None, italic=None, underline=None):
        if name is not None:
            self.set_font_name(name)
        if size is not None:
            self.set_font_size(size)
        self.set_font_style(bold, italic, underline)

    def add_paragraph(self, text, bold=None, italic=None, underline=None):
        prev_style = self.__font_styles.copy()
        self.set_font_style(bold, italic, underline)
        self.__pdf.multi_cell(w=0, text=text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_font_style(**prev_style)

    def save(self, filename):
        self.__pdf.output(filename)
