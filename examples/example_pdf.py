from docs import PDF
from docs.structs import Settings, Image, Table, NumberedList, BulletedList, Formula

file = PDF()

file.set_margin(top=1, right=3, bottom=1, left=1.25)

main_settings = Settings(
    font_name="Arial",
    font_size=14,
    alignment="left",
    bold=False,
    italic=False,
    underline=False
)
file.set_settings(**main_settings.get())
file.set_fixed_paragraph_spacing(spacing=0.5)

file.add_paragraph(
    text="Eat some more of these soft French rolls and drink some tea",
    bold=True
)

file.add_paragraph(
    text="Eat some more of these soft French rolls and drink some tea",
    font_size=30,
    italic=True
)

image_settings = Settings(font_size=10, alignment="center", underline=True)

image = Image("square.jpeg")
image.set_settings(image_settings)
file.add_image(
    image=image,
    image_width=10,
    image_height=6,
    image_alignment="center",
    image_spacing=1,
    caption="This is a square",
    caption_spacing=0.1
)

cell_settings = Settings(italic=True, bold=True, alignment="center")

table = Table([
    ["first cell", "second cell"],
    ["third cell", "fourth cell"]
])
table.set_settings(1, 1, cell_settings)
table.set_settings(2, 2, cell_settings)
file.add_table(
    table=table,
    table_width=15,
    table_height=1,
    table_alignment="center"
)

list_settings = Settings(bold=True, italic=True)

numbered_list = NumberedList(
    data=[
        "This is first sentence. This is first sentence. This is first sentence. This is first sentence. This is first sentence. This is first sentence. This is first sentence. This is first sentence.",
        "This is second sentence.",
        "This is third sentence."
    ],
    number_string="({i})",
    number_start=2,
    number_increment=3,
    between_spacing=0.1
)
numbered_list.set_number_settings(list_settings)
file.add_numbered_list(
    numbered_list=numbered_list,
    spacing=1
)

bulleted_list = BulletedList(
    data=[
        "This is first sentence. This is first sentence. This is first sentence. This is first sentence. This is first sentence. This is first sentence. This is first sentence. This is first sentence.",
        "This is second sentence.",
        "This is third sentence."
    ],
    between_spacing=0.1,
    indent=1.25
)
bulleted_list.set_bullet_settings(list_settings)
file.add_bulleted_list(
    bulleted_list=bulleted_list,
    spacing=1
)

formula_settings = Settings(italic=True, underline=True)
formula = Formula(
    formula="x^n + y^n = z^n"
)
formula.set_settings(formula_settings)
file.add_formula(
    formula=formula,
    formula_alignment="center"
)

file.save("example_pdf.pdf")
