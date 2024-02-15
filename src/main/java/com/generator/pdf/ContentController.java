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

        pdfGenerator.closeDocument();
        System.out.println("PDF document has been generated.");
    }

    private void handleCommand(String commandLine) {
        String[] parts = commandLine.split(" ", 2);
        if (parts.length != 2) {
            System.out.println("Invalid command format. Use 'code content'.");
            return;
        }

        String code = parts[0].trim();
        String content = parts[1].trim();

        try {
            switch (code) {
                case "b1":
                    pdfGenerator.addHeading(content, translator, 1);
                    break;
                case "b2":
                    pdfGenerator.addHeading(content, translator, 2);
                    break;
                case "c1":
                case "c2":
                    pdfGenerator.addParagraph(content, translator);
                    break;
                case "d2":
                    // TODO: список
                    System.out.println("List items are not implemented yet.");
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
