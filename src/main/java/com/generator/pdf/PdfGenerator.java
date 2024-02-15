package com.generator.pdf;

import com.itextpdf.kernel.pdf.PdfDocument;
import com.itextpdf.kernel.pdf.PdfWriter;
import com.itextpdf.layout.Document;
import com.itextpdf.layout.element.Paragraph;
import com.itextpdf.layout.properties.TextAlignment;
import com.itextpdf.kernel.font.PdfFont;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.io.IOException;

public class PdfGenerator {
    private Document document;
    private static final Logger logger = LoggerFactory.getLogger(PdfGenerator.class);

    public PdfGenerator(String dest) throws IOException {
        PdfWriter writer = new PdfWriter(dest);
        PdfDocument pdf = new PdfDocument(writer);
        this.document = new Document(pdf);
    }

    public void addHeading(String content, GostTranslator translator, int level) throws IOException {
        PdfFont font = FontMapper.getFont(translator.getFontName());
        float size = translator.getFontSize();
        TextAlignment alignment = TextAlignment.CENTER;

        if (level == 1) {
            size += 6;
        } else if (level == 2) {
            size += 4;
            alignment = TextAlignment.LEFT;
        }

        Paragraph paragraph = new Paragraph(content)
                .setFont(font)
                .setFontSize(size)
                .setTextAlignment(alignment);

        document.add(paragraph);
    }

    public void addParagraph(String content, GostTranslator translator) throws IOException {
        PdfFont font = FontMapper.getFont(translator.getFontName());
        Paragraph paragraph = new Paragraph(content)
                .setFont(font)
                .setFontSize(translator.getFontSize())
                .setFirstLineIndent(translator.getParagraphIndent())
                .setMarginLeft(translator.getMarginLeft())
                .setMarginRight(translator.getMarginRight())
                .setTextAlignment(TextAlignment.JUSTIFIED);

        document.add(paragraph);
    }

    public void closeDocument() {
        if (document != null) {
            document.close();
            logger.info("PDF document has been closed successfully.");
        }
    }
}
