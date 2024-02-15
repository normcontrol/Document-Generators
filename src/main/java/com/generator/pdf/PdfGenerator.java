package com.generator.pdf;

import com.itextpdf.kernel.pdf.PdfDocument;
import com.itextpdf.kernel.pdf.PdfWriter;
import com.itextpdf.layout.Document;
import com.itextpdf.layout.element.Paragraph;
import com.itextpdf.kernel.font.PdfFont;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.io.IOException;

public class PdfGenerator {

    private static final Logger logger = LoggerFactory.getLogger(PdfGenerator.class);

    public void createPdf(String dest, String fontName) {
        try {
            PdfWriter writer = new PdfWriter(dest);
            PdfDocument pdf = new PdfDocument(writer);
            Document document = new Document(pdf);

            PdfFont font = FontMapper.getFont(fontName);

            Paragraph paragraph = new Paragraph("Съешьте ещё этих мягких французских булок, да выпейте чаю.")
                    .setFont(font)
                    .setFontSize(12);
            document.add(paragraph);

            document.close();
            logger.info("PDF document has been generated successfully.");
        } catch (IOException e) {
            logger.error("Error while generating PDF: {}", e.getMessage());
        }
    }
}
