package com.generator.pdf;

import java.util.Scanner;

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
                // TODO: обработка других кодов
                default:
                    System.out.println("Unknown command code: " + code);
                    break;
            }
        } catch (Exception e) {
            System.err.println("Error processing command '" + commandLine + "': " + e.getMessage());
        }
    }

}
