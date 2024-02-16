package com.generator.pdf;

import java.util.Scanner;
import java.nio.file.Path;
import java.nio.file.Files;
import java.io.IOException;
import java.awt.image.BufferedImage;


import com.itextpdf.layout.properties.HorizontalAlignment;

public class ContentController {
    private final PdfGenerator pdfGenerator;
    private final GostTranslator translator;
    private final Scanner scanner = new Scanner(System.in);

    public ContentController(PdfGenerator pdfGenerator, GostTranslator translator) {
        this.pdfGenerator = pdfGenerator;
        this.translator = translator;
    }

    public void start() {
        System.out.println("Enter content commands ('end' to finish):");
        String line;
        while (!(line = scanner.nextLine()).equalsIgnoreCase("end")) {
            handleCommand(line);
        }

        pdfGenerator.finalizeList();
        pdfGenerator.closeDocument();
        System.out.println("PDF document has been generated.");
    }

    private void handleCommand(String commandLine) {
        String[] parts = commandLine.trim().split(" ", 2);
        String code = parts[0];

        String content = parts.length > 1 ? parts[1] : "";

        try {
            switch (code) {
                case "b1":
                    pdfGenerator.addHeading(content, translator, 1);
                    break;
                case "b2":
                    pdfGenerator.addHeading(content, translator, 2);
                    break;
                case "c1":
                    pdfGenerator.addParagraph(content, translator);
                    break;
                case "c2":
                case "d2":
                    if (!content.isEmpty()) {
                        pdfGenerator.addListItem(content);
                        System.out.println("Элемент списка добавлен. Для завершения списка введите 'd3'.");
                    } else {
                        System.out.println("Для добавления элемента списка введите 'd2 (текст элемента)'.");
                    }
                    break;
                case "d3":
                    pdfGenerator.finalizeList();
                    System.out.println("Список завершен.");
                    break;
                default:
                    System.out.println("Unknown command code: " + code);
                    break;
                case "f1":
                    int numColumns = Integer.parseInt(content);
                    pdfGenerator.startTable(numColumns, null);
                    break;
                case "f2":
                    pdfGenerator.setTableCaption(content);
                    System.out.println("Установлена подпись для следующей таблицы: " + content);
                    break;
                case "f3":
                    pdfGenerator.addCellToTable(content);
                    break;
                case "f4":
                    pdfGenerator.finalizeTable();
                    System.out.println("Таблица завершена.");
                    break;
                case "img":
                    if (content.isEmpty() || content.split(" ").length < 4) {
                        System.out.println("Для вставки изображения необходимо передать параметры в формате: img <путь к изображению> <ширина> <высота> <выравнивание>");
                        System.out.println("Доступные значения для выравнивания: left, center, right");
                        System.out.println("Пример: img /path/to/image.jpg 200 100 center");
                    } else {
                        String[] params = content.split(" ");
                        try {
                            String imagePath = params[0];
                            float width = Float.parseFloat(params[1]);
                            float height = Float.parseFloat(params[2]);
                            String alignment = params[3].toLowerCase();

                            pdfGenerator.addImage(imagePath, width, height, alignment);
                            System.out.println("Изображение добавлено с выравниванием: " + alignment);
                        } catch (Exception e) {
                            System.err.println("Ошибка при добавлении изображения: " + e.getMessage());
                        }
                    }
                    break;
                case "latex":
                    if (content.isEmpty()) {
                        System.out.println("Необходимо предоставить LaTeX формулу.");
                    } else {
                        try {
                            BufferedImage latexImage = LaTeXToImage.latexToImage(content);
                            Path tempImagePath = LaTeXToImage.saveImageToFile(latexImage);

                            String alignmentStr = "center";

                            pdfGenerator.addImage(tempImagePath.toString(), 70, 50, alignmentStr);
                            System.out.println("Формула добавлена в документ.");

                            Files.delete(tempImagePath);
                        } catch (IOException e) {
                            System.err.println("Ошибка при создании изображения из LaTeX: " + e.getMessage());
                        }
                    }
                    break;
            }
        } catch (Exception e) {
            System.err.println("Error processing command '" + commandLine + "': " + e.getMessage());
        }
    }

}
