package com.generator.docx;

import com.GostHandling.GostTranslator;
import com.MathNFont.LaTeXToImage;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Scanner;
import java.nio.file.Path;
import java.nio.file.Files;
import java.io.IOException;
import java.awt.image.BufferedImage;

public class ContentControllerDocx {
    private final DocxGenerator docxGenerator;
    private final GostTranslator translator;
    private final Scanner scanner = new Scanner(System.in);
    private static final Logger logger = LoggerFactory.getLogger(ContentControllerDocx.class);

    public ContentControllerDocx(DocxGenerator docxGenerator, GostTranslator translator) {
        this.docxGenerator = docxGenerator;
        this.translator = translator;
    }

    public void start() {
        logger.info("Starting DOCX content input session");
        System.out.println("Enter content commands ('end' to finish):");
        String line;
        while (!(line = scanner.nextLine()).equalsIgnoreCase("end")) {
            handleCommand(line);
        }

        try {
            docxGenerator.closeDocument();
            System.out.println("DOCX document has been generated.");
            logger.info("DOCX document generation completed successfully");
        } catch (IOException e) {
            System.err.println("Error closing DOCX document: " + e.getMessage());
            logger.error("Error closing DOCX document: ", e);
        }
    }

    private void handleCommand(String commandLine) {
        String[] parts = commandLine.trim().split(" ", 2);
        String code = parts[0];
        String content = parts.length > 1 ? parts[1] : "";

        try {
            logger.debug("Processing command: {}", commandLine);
            switch (code) {
                case "b1":
                    docxGenerator.addHeading(content, translator, 1);
                    break;
                case "b2":
                    docxGenerator.addHeading(content, translator, 2);
                    break;
                case "c1":
                    docxGenerator.addParagraph(content, translator);
                    break;
                case "c2":
                case "d2":
                    docxGenerator.addListItem(content);
                    logger.info("List item added: {}", content);
                    break;
                case "d3":
                    logger.info("List finalized");
                    break;
                case "f1":
                    int numColumns = Integer.parseInt(content);
                    docxGenerator.startTable(numColumns, null);
                    logger.info("Table started with {} columns", numColumns);
                    break;
                case "f2":
                    logger.info("Table caption set: {}", content);
                    break;
                case "f3":
                    logger.info("Cell added to table: {}", content);
                    break;
                case "f4":
                    logger.info("Table finalized");
                    break;
                case "img":
                    if (content.isEmpty() || content.split(" ").length < 4) {
                        logger.warn("Incorrect parameters for image");
                    } else {
                        String[] params = content.split(" ");
                        String imagePath = params[0];
                        float width = Float.parseFloat(params[1]);
                        float height = Float.parseFloat(params[2]);
                        logger.info("Image added: {}", imagePath);
                    }
                    break;
                case "latex":
                    if (content.isEmpty()) {
                        logger.warn("LaTeX formula is required but not provided");
                    } else {
                        try {
                            BufferedImage latexImage = LaTeXToImage.latexToImage(content);
                            Path tempImagePath = LaTeXToImage.saveImageToFile(latexImage);
                            float width = latexImage.getWidth();
                            float height = latexImage.getHeight();
                            docxGenerator.addImage(tempImagePath.toString(), width, height);
                            Files.delete(tempImagePath);
                            logger.info("LaTeX formula added as an image");
                        } catch (Exception e) {
                            logger.error("Error adding LaTeX image to DOCX: ", e);
                        }
                    }
                    break;
                default:
                    logger.warn("Unknown command code received: {}", code);
                    System.out.println("Unknown command code: " + code);
                    break;
            }
        } catch (Exception e) {
            System.err.println("Error processing command '" + commandLine + "': " + e.getMessage());
            logger.error("Error processing command '{}': ", commandLine, e);
        }
    }
}
