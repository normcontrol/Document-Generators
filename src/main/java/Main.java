import com.GostHandling.GostSelector;
import com.generator.pdf.ContentController;
import com.generator.docx.ContentControllerDocx;
import com.generator.pdf.PdfGenerator;
import com.generator.docx.DocxGenerator;
import com.GostHandling.GostTranslator;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.util.Map;
import java.util.Scanner;

public class Main {
    private static final Logger logger = LoggerFactory.getLogger(Main.class);

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Choose document format: PDF, DOCX");
        String format = scanner.nextLine().toUpperCase();

        if (!format.equals("PDF") && !format.equals("DOCX")) {
            System.out.println(format + " format support is TODO.");
            return;
        }

        Map<String, Object> gostDetails = GostSelector.selectGost();
        if (gostDetails == null) {
            System.out.println("Document generation was cancelled due to GOST selection failure.");
            return;
        }
        GostTranslator translator = new GostTranslator(gostDetails);

        try {
            switch (format) {
                case "PDF":
                    PdfGenerator pdfGenerator = new PdfGenerator("docs/custom_document.pdf");
                    ContentController contentController = new ContentController(pdfGenerator, translator);
                    contentController.start();
                    System.out.println("PDF document has been generated.");
                    break;
                case "DOCX":
                    DocxGenerator docxGenerator = new DocxGenerator("docs/custom_document.docx");
                    ContentControllerDocx contentControllerDocx = new ContentControllerDocx(docxGenerator, translator);
                    contentControllerDocx.start();
                    System.out.println("DOCX document has been generated.");
                    break;
                default:
                    break;
            }
        } catch (IOException e) {
            logger.error("Error initializing document generation: ", e);
        }
    }
}

