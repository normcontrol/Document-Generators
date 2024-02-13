from docs import PDF, Settings

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

image_settings = Settings(
    font_size=10,
    alignment="center",
    underline=True
)
pdf.add_image(
    "https://blockchainmedia.id/wp-content/uploads/2021/11/Square-Whitepaper-DEX-Bitcoin-Bursa-Terdesentralisasi.jpeg",
    image_width=100,
    image_height=50,
    image_alignment="center",
    text="This is a square",
    spacing=2,
    **image_settings.get()
)

pdf.add_paragraph(
    "Eat some more of these soft French rolls and drink some tea",
    spacing=10
)

pdf.save("example.pdf")
