from docs import PDF

pdf = PDF()

pdf.set_font_name("Arial")
pdf.set_font_size(14)
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

pdf.add_image(
    "https://blockchainmedia.id/wp-content/uploads/2021/11/Square-Whitepaper-DEX-Bitcoin-Bursa-Terdesentralisasi.jpeg",
    image_width=100,
    image_height=50,
    caption_text="this is a square",
    caption_spacing=2,
    caption_font_size=10,
    caption_underline=True
)

pdf.add_paragraph(
    "Eat some more of these soft French rolls and drink some tea",
    spacing=10
)

pdf.save("example.pdf")
