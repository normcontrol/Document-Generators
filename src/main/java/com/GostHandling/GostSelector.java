package com.GostHandling;

import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class GostSelector {
    public static Map<String, Object> selectGost() {
        Set<String> availableGosts = GostReader.loadAvailableGosts("/gost.json");
        System.out.println("Available GOSTs:");
        availableGosts.forEach(System.out::println);

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter GOST name: ");
        String selectedGost = scanner.nextLine();

        if (availableGosts.contains(selectedGost)) {
            System.out.println("You selected: " + selectedGost);
            return GostReader.loadGostConfig("/gost.json", selectedGost);
        } else {
            System.out.println("GOST not found.");
            return null;
        }
    }
}




