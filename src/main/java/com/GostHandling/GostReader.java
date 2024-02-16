package com.GostHandling;

import com.google.gson.Gson;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Map;
import java.util.Set;

public class GostReader {
    public static Set<String> loadAvailableGosts(String resourcePath) {
        Gson gson = new Gson();
        try (InputStream is = GostReader.class.getResourceAsStream(resourcePath);
             InputStreamReader isr = new InputStreamReader(is)) {
            Map<String, Object> allGosts = gson.fromJson(isr, Map.class);
            return allGosts.keySet();
        } catch (Exception e) {
            throw new RuntimeException("Failed to load GOST config", e);
        }
    }

    public static Map<String, Object> loadGostConfig(String resourcePath, String gostName) {
        Gson gson = new Gson();
        try (InputStream is = GostReader.class.getResourceAsStream(resourcePath);
             InputStreamReader isr = new InputStreamReader(is)) {
            Map<String, Object> allGosts = gson.fromJson(isr, Map.class);
            if (allGosts.containsKey(gostName)) {
                return (Map<String, Object>) allGosts.get(gostName);
            } else {
                throw new IllegalArgumentException("GOST " + gostName + " not found in config");
            }
        } catch (Exception e) {
            throw new RuntimeException("Failed to load GOST config", e);
        }
    }
}