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
import com.itextpdf.layout.element.Table;
import com.itextpdf.layout.element.Cell;
import com.itextpdf.layout.element.Image;
import com.itextpdf.layout.properties.HorizontalAlignment;
import com.itextpdf.io.image.ImageData;
import com.itextpdf.io.image.ImageDataFactory;

public class PdfGenerator {
    private String tableCaption = null;
    private Table currentTable;
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

    public void startTable(int numColumns, String caption) {
        if (currentTable == null) {
            currentTable = new Table(numColumns);
            logger.info("Начата новая таблица с количеством столбцов: " + numColumns);

            if (caption != null && !caption.isEmpty()) {
                document.add(new Paragraph(caption));
                logger.info("К таблице добавлена подпись: " + caption);
            }
        } else {
            logger.warn("Попытка начать новую таблицу без завершения текущей.");
        }
    }

    public void addCellToTable(String content) {
        if (currentTable != null) {
            currentTable.addCell(new Cell().add(new Paragraph(content)));
            logger.info("В таблицу добавлена ячейка с содержимым: " + content);
        } else {
            logger.error("Ошибка: попытка добавить ячейку в неинициализированную таблицу.");
            System.err.println("Table is not initialized.");
        }
    }

    public void setTableCaption(String caption) {
        this.tableCaption = caption;
        logger.info("Установлена подпись для таблицы: " + caption);
    }

    public void finalizeTable() {
        if (currentTable != null) {
            document.add(currentTable);
            if (tableCaption != null && !tableCaption.isEmpty()) {
                document.add(new Paragraph(tableCaption));
                logger.info("Под таблицей добавлена подпись: " + tableCaption);
                tableCaption = null;
            }
            currentTable = null;
            logger.info("Таблица завершена и добавлена в документ.");
        } else {
            logger.warn("Попытка завершить несуществующую таблицу.");
        }
    }

    public void addImage(String imagePath, float width, float height, HorizontalAlignment alignment) throws IOException {
        ImageData data = ImageDataFactory.create(imagePath);
        Image image = new Image(data).setWidth(width).setHeight(height).setHorizontalAlignment(alignment);
        document.add(image);
        logger.info("Добавлено изображение: " + imagePath);
    }

    public void closeDocument() {
        finalizeList();
        finalizeTable();
        if (document != null) {
            document.close();
            logger.info("PDF document has been closed successfully.");
        }
    }
}
