from fpdf import FPDF
from fpdf.enums import Align


class PDF:
    def __init__(
        self
    ) -> None:
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
        self.__first_addition = True
        self.__fixed_paragraph_spacing = None
        self.__pdf.add_page()

    def set_font_name(
        self,
        name: str
    ) -> None:
        self.__font_name = name
        self.__pdf.set_font(name, self.__pdf.font_style, self.__font_size)

    def set_font_size(
        self,
        size: float
    ) -> None:
        self.__font_size = size
        self.__pdf.set_font_size(size)

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

    def set_font(
        self,
        name: str = None,
        size: float = None,
        bold: bool = None,
        italic: bool = None,
        underline: bool = None
    ) -> None:
        if name is not None:
            self.set_font_name(name)
        if size is not None:
            self.set_font_size(size)
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
        alignment: str = "left",
        spacing: float = None,
        font_name: str = None,
        font_size: float = None,
        bold: bool = None,
        italic: bool = None,
        underline: bool = None
    ) -> None:
        last_font_name = self.__font_name
        last_font_size = self.__font_size
        last_font_styles = self.__font_styles.copy()
        self._add_spacing(spacing)
        self.set_font(font_name, font_size, bold, italic, underline)
        self.__pdf.multi_cell(w=0, h=self.__line_spacing * self.__pdf.font_size, text=text, align=self._make_alignment(alignment))
        print(last_font_styles, self.__font_styles)
        self.set_font(last_font_name, last_font_size, **last_font_styles)

    def add_image(
        self,
        image_path: str,
        image_width: float = None,
        image_height: float = None,
        image_alignment: str = "center",
        caption_text: str = None,
        caption_spacing: float = None,
        caption_alignment: str = "center",
        caption_font_name: str = None,
        caption_font_size: float = None,
        caption_bold: bool = None,
        caption_italic: bool = None,
        caption_underline: bool = None
    ) -> None:
        width = 0 if image_width is None else image_width
        height = 0 if image_height is None else image_height
        self._add_spacing()
        self.__pdf.image(image_path, x=self._make_alignment(image_alignment), w=width, h=height)
        if caption_text is not None:
            self.add_paragraph(
                caption_text,
                caption_alignment,
                caption_spacing,
                caption_font_name,
                caption_font_size,
                caption_bold,
                caption_italic,
                caption_underline
            )

    def save(
        self,
        filename: str
    ) -> None:
        self.__pdf.output(filename)

    def _add_spacing(
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

    @staticmethod
    def _make_alignment(
        alignment
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
