package com.generator.pdf;

import java.util.Map;

public class GostTranslator {
    private String fontName;
    private float fontSize;
    private float marginLeft, marginRight, marginTop, marginBottom;
    private String alignmentText;
    private float lineSpacing;
    private float paragraphIndent;

    public GostTranslator(Map<String, Object> gostDetails) {
        this.fontName = (String) gostDetails.get("fontName");
        this.fontSize = ((Number) gostDetails.get("fontSize")).floatValue();

        Map<String, Number> margins = (Map<String, Number>) gostDetails.get("margins");
        this.marginLeft = margins.get("left").floatValue();
        this.marginRight = margins.get("right").floatValue();
        this.marginTop = margins.get("top").floatValue();
        this.marginBottom = margins.get("bottom").floatValue();

        Map<String, String> alignment = (Map<String, String>) gostDetails.get("alignment");
        this.alignmentText = alignment.get("text");

        this.lineSpacing = Float.parseFloat(gostDetails.get("lineSpacing").toString());
        this.paragraphIndent = Float.parseFloat(gostDetails.get("paragraphIndent").toString());
    }

    public String getFontName() { return fontName; }
    public float getFontSize() { return fontSize; }
    public float getMarginLeft() { return marginLeft; }
    public float getMarginRight() { return marginRight; }
    public float getMarginTop() { return marginTop; }
    public float getMarginBottom() { return marginBottom; }
    public String getAlignmentText() { return alignmentText; }
    public float getLineSpacing() { return lineSpacing; }
    public float getParagraphIndent() { return paragraphIndent; }

}
