package com.generator.pdf;

import org.scilab.forge.jlatexmath.TeXConstants;
import org.scilab.forge.jlatexmath.TeXFormula;
import org.scilab.forge.jlatexmath.TeXIcon;
import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class LaTeXToImage {
    public static BufferedImage latexToImage(String latex) {
        TeXFormula formula = new TeXFormula(latex);
        TeXIcon icon = formula.createTeXIcon(TeXConstants.STYLE_DISPLAY, 20);

        icon.setInsets(new Insets(5, 5, 5, 5));

        BufferedImage image = new BufferedImage(icon.getIconWidth(), icon.getIconHeight(), BufferedImage.TYPE_INT_ARGB);
        Graphics2D g2 = image.createGraphics();
        g2.setColor(Color.WHITE);
        g2.fillRect(0,0,icon.getIconWidth(),icon.getIconHeight());
        JLabel jl = new JLabel();
        jl.setForeground(new Color(0, 0, 0));
        icon.paintIcon(jl, g2, 0, 0);

        return image;
    }

    public static Path saveImageToFile(BufferedImage image) throws IOException {
        Path tempFile = Files.createTempFile("latex_formula", ".png");
        ImageIO.write(image, "png", tempFile.toFile());
        return tempFile;
    }
}
