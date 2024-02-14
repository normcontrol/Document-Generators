from docs import PDF
from docs.structs import Settings, Image, Table, NumberedList, BulletedList

pdf = PDF()

main_settings = Settings(
    font_name="Arial",
    font_size=14,
    alignment="left",
    bold=False,
    italic=False,
    underline=False
)
pdf.set_settings(**main_settings.get())
pdf.set_fixed_paragraph_spacing(5)

pdf.add_paragraph(
    "Eat some more of these soft French rolls and drink some tea",
    bold=True
)

pdf.add_paragraph(
    "Eat some more of these soft French rolls and drink some tea",
    font_size=30,
    italic=True
)

image_settings = Settings(font_size=10, alignment="center", underline=True)
image = Image("https://blockchainmedia.id/wp-content/uploads/2021/11/Square-Whitepaper-DEX-Bitcoin-Bursa-Terdesentralisasi.jpeg")
image.set_settings(image_settings)
pdf.add_image(image, image_width=100, image_height=50, text="This is a square", text_spacing=1)

pdf.add_paragraph(
    "Eat some more of these soft French rolls and drink some tea",
    spacing=10
)

table = Table([
    ["first cell", "second cell"],
    ["third cell", "fourth cell"]
])
cell_settings = Settings(italic=True, bold=True, alignment="center")
table.set_settings(1, 1, cell_settings)
table.set_settings(2, 2, cell_settings)
pdf.add_table(table)

list_settings = Settings(bold=True, font_size=20, alignment="center")

numbered_list = NumberedList(
    [
        "This is first sentence. This is first sentence. This is first sentence. This is first sentence. This is first sentence. This is first sentence. This is first sentence. This is first sentence.",
        "This is second sentence.",
        "This is third sentence."
    ],
    number_string="({i})",
    number_start=2,
    number_increment=3,
    between_spacing=1
)
numbered_list.set_number_settings(list_settings)
pdf.add_numbered_list(numbered_list, spacing=15)

bulleted_list = BulletedList(
    [
        "This is first sentence. This is first sentence. This is first sentence. This is first sentence. This is first sentence. This is first sentence. This is first sentence. This is first sentence.",
        "This is second sentence.",
        "This is third sentence."
    ],
    between_spacing=1
)
bulleted_list.set_bullet_settings(list_settings)
pdf.add_bulleted_list(bulleted_list, spacing=15)

pdf.add_paragraph(
    "Eat some more of these soft French rolls and drink some tea"
)

pdf.save("example_pdf.pdf")
