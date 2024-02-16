package com.generator.docx;

import com.GostHandling.GostTranslator;
import org.apache.poi.xwpf.usermodel.*;
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.util.Units;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.FileOutputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.math.BigInteger;

public class DocxGenerator {
    private XWPFDocument document;
    private String filePath;
    private static final Logger logger = LoggerFactory.getLogger(DocxGenerator.class);

    public DocxGenerator(String dest) throws IOException {
        this.filePath = dest;
        this.document = new XWPFDocument();
        try (FileOutputStream out = new FileOutputStream(dest)) {
            document.write(out);
        }
    }

    public void addHeading(String content, GostTranslator translator, int level) {
        XWPFParagraph paragraph = document.createParagraph();
        XWPFRun run = paragraph.createRun();
        run.setText(content);
        switch (level) {
            case 1:
                run.setBold(true);
                run.setFontSize(14);
                paragraph.setAlignment(ParagraphAlignment.CENTER);
                break;
            case 2:
                run.setBold(true);
                run.setFontSize(12);
                paragraph.setAlignment(ParagraphAlignment.LEFT);
                break;
            default:
                run.setFontSize(10);
                paragraph.setAlignment(ParagraphAlignment.LEFT);
                break;
        }
    }

    public void addParagraph(String content, GostTranslator translator) {
        XWPFParagraph paragraph = document.createParagraph();
        XWPFRun run = paragraph.createRun();
        run.setText(content);
        paragraph.setAlignment(ParagraphAlignment.BOTH);
    }

    public void addListItem(String content) {
        XWPFParagraph paragraph = document.createParagraph();
        XWPFRun run = paragraph.createRun();
        run.setText("• " + content);
    }

    public void startTable(int numColumns, String caption) {
        XWPFTable table = document.createTable(1, numColumns);
        if (caption != null && !caption.isEmpty()) {
            XWPFParagraph p = document.createParagraph();
            XWPFRun run = p.createRun();
            run.setText(caption);
            run.setBold(true);
        }
    }

    public void addImage(String imagePath, float width, float height) throws Exception {
        FileInputStream is = new FileInputStream(imagePath);
        XWPFParagraph paragraph = document.createParagraph();
        XWPFRun run = paragraph.createRun();
        run.addPicture(is, XWPFDocument.PICTURE_TYPE_JPEG, imagePath, Units.toEMU(width), Units.toEMU(height));
        is.close();
    }

    public void closeDocument() throws IOException {
        try (FileOutputStream out = new FileOutputStream(this.filePath)) {
            document.write(out);
        }
        logger.info("DOCX document has been closed successfully.");
    }
}

