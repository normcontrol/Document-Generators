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
import com.itextpdf.layout.element.List;
import com.itextpdf.layout.element.ListItem;

public class PdfGenerator {
    private List list;
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

    private void startNewList() {
        if (this.list == null) {
            this.list = new List();
        }
    }

    public void addListItem(String content) throws IOException {
        startNewList();
        ListItem listItem = new ListItem(content);
        this.list.add(listItem);
    }

    public void finalizeList() {
        if (this.list != null && !this.list.isEmpty()) {
            document.add(this.list);
            this.list = new List();
        }
    }

    public void closeDocument() {
        if (document != null) {
            document.close();
            logger.info("PDF document has been closed successfully.");
        }
    }
}
