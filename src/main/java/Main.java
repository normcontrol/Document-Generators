import com.GostHandling.GostSelector;
import com.generator.pdf.PdfGenerator;
import com.generator.pdf.GostTranslator;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Map;
import java.util.Scanner;

public class Main {
    private static final Logger logger = LoggerFactory.getLogger(Main.class);

    public static void main(String[] args) {
        System.out.println("Choose document format: ODT, PDF, DOCX");
        Scanner scanner = new Scanner(System.in);
        String format = scanner.nextLine().toUpperCase();

        if ("PDF".equals(format)) {
            Map<String, Object> gostDetails = GostSelector.selectGost();
            if (gostDetails != null) {
                logger.info("Selected GOST details: {}", gostDetails);


                System.out.println("Enter the text for your document:");
                String customText = scanner.nextLine();

                GostTranslator translator = new GostTranslator(gostDetails);

                PdfGenerator pdfGenerator = new PdfGenerator();
                pdfGenerator.createPdf("docs/custom_document.pdf", translator.getFontName(), customText);
                System.out.println("PDF document with custom text has been generated.");
            } else {
                System.out.println("PDF generation was cancelled due to GOST selection failure.");
            }
        } else {
            System.out.println(format + " format support is TODO.");
        }
    }
}
