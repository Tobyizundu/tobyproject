package SE3.gui;
import javax.swing.*;
import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;
import SE3.api.Translate;

public class ButtonListener implements DocumentListener {
    private final JComboBox<String> fromComboBox;
    private final JComboBox<String> toComboBox;
    private final JTextArea fromTextArea;
    private final JTextArea toTextArea;
    private final Translate translator;

    public ButtonListener(JComboBox<String> fromComboBox, JComboBox<String> toComboBox, JTextArea fromTextArea, JTextArea toTextArea) {
        this.fromComboBox = fromComboBox;
        this.toComboBox = toComboBox;
        this.fromTextArea = fromTextArea;
        this.toTextArea = toTextArea;

        // Initialize the translator
        try {
            this.translator = new Translate();
        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException("Failed to initialize translator");
        }

        // Add document listener to JTextArea to trigger translation on text change
        fromTextArea.getDocument().addDocumentListener(this);
    }

    @Override
    public void insertUpdate(DocumentEvent e) {
        translateText();
    }

    @Override
    public void removeUpdate(DocumentEvent e) {
        translateText();
    }

    @Override
    public void changedUpdate(DocumentEvent e) {
        // Plain text components do not fire these events
    }

    private void translateText() {
        String sourceLang = (String) fromComboBox.getSelectedItem();
        String targetLang = (String) toComboBox.getSelectedItem();
        String textToTranslate = fromTextArea.getText();

        // Perform translation only if source and target languages are selected and there is text to translate
        if (sourceLang != null && targetLang != null && !textToTranslate.isEmpty()) {
            try {
                // Translate the text from the source language to the target language
                String translatedText = translator.translateText(sourceLang, targetLang, textToTranslate);
                // Set the translated text to the target JTextArea
                toTextArea.setText(translatedText);
            } catch (Exception ex) {
                // Handle translation error
                ex.printStackTrace();
                // Optionally, display an error message to the user
            }
        }
    }
}
