package com.generator.pdf;

import com.itextpdf.kernel.font.PdfFont;
import com.itextpdf.kernel.font.PdfFontFactory;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class FontMapper {
    private static final Logger logger = LoggerFactory.getLogger(FontMapper.class);
    private static final Map<String, String> fontMap = new HashMap<>();

    static {
        fontMap.put("Times New Roman", "src/main/resources/fonts/Times New Roman/timesnrcyrmt.ttf");
    }

    public static PdfFont getFont(String fontName) throws IOException {
        String fontPath = fontMap.getOrDefault(fontName, "src/main/resources/fonts/Times New Roman/timesnrcyrmt.ttf");
        logger.info("Using font file: {}", fontPath);
        return PdfFontFactory.createFont(fontPath, PdfFontFactory.EmbeddingStrategy.PREFER_EMBEDDED);
    }
}
