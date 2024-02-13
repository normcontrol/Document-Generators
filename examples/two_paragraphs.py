from docs import PDF

pdf = PDF()
pdf.set_font_size(12)
pdf.add_paragraph("Eat some more of these soft French rolls and drink some tea", italic=True)
pdf.set_font_size(30)
pdf.add_paragraph("Eat some more of these soft French rolls and drink some tea", underline=True)
pdf.save("hello_world.pdf")
