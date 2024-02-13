from docs import PDF

pdf = PDF()
pdf.set_font_size(12)
pdf.add_paragraph("Eat some more of these soft French rolls and drink some tea", alignment="center")
pdf.set_font_size(30)
pdf.set_font_style(italic=True, underline=True)
pdf.add_paragraph("Eat some more of these soft French rolls and drink some tea")
pdf.save("two_paragraphs.pdf")
