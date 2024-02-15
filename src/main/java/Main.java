import com.GostHandling.GostSelector;
import com.generator.pdf.ContentController;
import com.generator.pdf.PdfGenerator;
import com.generator.pdf.GostTranslator;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.util.Map;
import java.util.Scanner;

public class Main {
    private static final Logger logger = LoggerFactory.getLogger(Main.class);

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Choose document format: ODT, PDF, DOCX");
        String format = scanner.nextLine().toUpperCase();

        if (!"PDF".equals(format)) {
            System.out.println(format + " format support is TODO.");
            return;
        }

        Map<String, Object> gostDetails = GostSelector.selectGost();
        if (gostDetails == null) {
            System.out.println("PDF generation was cancelled due to GOST selection failure.");
            return;
        }
        GostTranslator translator = new GostTranslator(gostDetails);

        try {
            PdfGenerator pdfGenerator = new PdfGenerator("docs/custom_document_type5.pdf");
            ContentController contentController = new ContentController(pdfGenerator, translator);
            contentController.start();
            System.out.println("PDF document has been generated.");
        } catch (IOException e) {
            logger.error("Error initializing PDF generation: ", e);
        }
    }
}
