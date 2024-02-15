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

        switch (format) {
            case "PDF":
                Map<String, Object> gostDetails = GostSelector.selectGost();
                if (gostDetails != null) {
                    logger.info("Selected GOST details: {}", gostDetails);

                    GostTranslator translator = new GostTranslator(gostDetails);

                    PdfGenerator pdfGenerator = new PdfGenerator();
                    pdfGenerator.createPdf("docs/document.pdf", translator.getFontName());
                    System.out.println("PDF document has been generated.");
                } else {
                    System.out.println("PDF generation was cancelled due to GOST selection failure.");
                }
                break;
            case "ODT":
            case "DOCX":
                System.out.println(format + " format support is TODO.");
                break;
            default:
                System.out.println("Unknown format: " + format);
                break;
        }
    }
}

