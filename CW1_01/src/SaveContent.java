import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

import javax.swing.JFileChooser;
import javax.swing.JOptionPane;
import javax.swing.JTextPane;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.text.BadLocationException;
import javax.swing.text.StyledDocument;
import javax.swing.text.html.HTMLEditorKit;

public class SaveContent {
	 String FormattedText;
	 public boolean save(JTextPane text) {
	        if (text.getText().length() > 0) {
	            JFileChooser chooser = new JFileChooser();
	            chooser.setMultiSelectionEnabled(false);
	            FileNameExtensionFilter filter = new FileNameExtensionFilter("Rich Text Format", "rtf");
	            chooser.setFileFilter(filter);

	            int option = chooser.showSaveDialog(null);
	            if (option == JFileChooser.APPROVE_OPTION) {
	                String filepath = chooser.getSelectedFile().getPath();
	                if (!filepath.toLowerCase().endsWith(".rtf")) {
	                    filepath = filepath + ".rtf";
	                }

	                File file = new File(filepath);
	                if (file.exists()) {  
	                	int overwriteOption = JOptionPane.showConfirmDialog(null,
	                            "The file already exists. Do you want to overwrite it?", "Confirm Overwrite",
	                            JOptionPane.YES_NO_OPTION);
	                    if (overwriteOption != JOptionPane.YES_OPTION) {
	                        return false; // User cancelled the save operation
	                    }
	                }

	                try {
	                    StyledDocument doc = (StyledDocument) text.getDocument();
	                    HTMLEditorKit kit = new HTMLEditorKit();
	                    try (BufferedOutputStream out = new BufferedOutputStream(new FileOutputStream(filepath))) {
	                        kit.write(out, doc, doc.getStartPosition().getOffset(), doc.getLength());
	                    } catch (IOException e) {
	                        e.printStackTrace();
	                        // Handle the IO exception appropriately.
	                    }
	                } catch (BadLocationException e) {
	                    e.printStackTrace();
	                    // Handle the BadLocationException appropriately.
	                }
	                return true; // Saved successfully
	            } else {
	                }
	            System.out.print("Save cancelled");
            }
        
        return false; // Nothing was saved
    }


	    


public static boolean exitApplication(JTextPane text) {
    if (hasUnsavedChanges(text)) {
        int response = JOptionPane.showConfirmDialog(null,
                "You have unsaved changes. Do you want to save them before exiting?",
                "Unsaved Changes", JOptionPane.YES_NO_CANCEL_OPTION);
        if (response == JOptionPane.YES_OPTION) {
            if (!new SaveContent().save(text)) {
                return false; // User canceled the save operation
            }
        } else if (response == JOptionPane.CANCEL_OPTION) {
            return false; // User canceled the exit operation
        }
    }
    return true; // Continue with exiting the application
}

public static boolean hasUnsavedChanges(JTextPane text) {
    StyledDocument doc = (StyledDocument) text.getDocument();
    return doc.getLength() > 0; // Check if there is any content in the document
}
}


	            






	 
	 
            
          
	  
	 