package SE3.api;
import com.deepl.api.*;

public class Translate {
    Translator translator;

    // constructor:
    public Translate() throws Exception {
        String authKey = "f34e8900-7184-4dfe-a243-88a721be8292:fx"; //authentication Key from Deepl. Replace with reference to file instead.
        translator = new Translator(authKey);
    }

    /**
     * Translates text from a source language to a target language using the DeepL API.
     *
     * @param sourceLang  The source language code (e.g., "EN" for English).
     * @param targetLang The target language code (e.g., "FR" for French).
     *                   These are not case-sensitive.
     *
     * @param transText  The text to be translated.
     * @return The translated text.
     * @throws Exception if there is an error during the translation process.
     */
    public String translateText(String sourceLang, String targetLang, String transText) throws Exception {
        try {   
            TextResult result = translator.translateText(transText, sourceLang, targetLang);
            return result.getText();
        } catch(DeepLException e){
            // Log error
            throw new Exception("Error during text translation:\n" + e.getMessage(), e);
        }
    }
}