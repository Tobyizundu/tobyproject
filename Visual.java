import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

import javax.swing.*;
import javax.swing.text.BadLocationException;
import javax.swing.text.Document;
import javax.swing.undo.UndoManager;

import java.io.File;

    public class Visual extends JPanel implements ActionListener {
    private JTextPane textRegion;
    private JButton SaveButton;
    private JComboBox colorCombo;
    private JComboBox fontCombo;
    private JComboBox styleCombo;
    private JLabel processorLabel;
    private JSlider fontSize;
    private JMenuBar menuBar;
    private JMenu fileMenu;
    private JMenu fileoperation1;
    private JMenu fileoperation2;
    private JMenuItem openFileItem;
    private JMenuItem insertTemplateItem; // Added Insert
    private JMenuItem insertTemplateItem2;
    private JFileChooser fileChooser; // Added file chooser for opening files
    private JLabel wordcount;
    private UndoManager undoManager;//
    // Create some method obj
    SaveContent saveFile = new SaveContent();
    Colorsetting colorClass = new Colorsetting();
    FontSetting fontClass = new FontSetting();
    Main word = new Main();

    // Create some array
    String[] colorItems = { "Red", "Blue", "Green", "Black" };
    String[] fontItem = { "Arial", "New time roman", "Monospaced", "Serif", "Sans serif" };
    
    
    public Visual() {
        init();
        setupUndoRedo();
    }

   
		
	private void  setupUndoRedo() {
		undoManager=new UndoManager();
		Document doc=textRegion.getDocument();
		
		doc.addUndoableEditListener(e -> {
            undoManager.addEdit(e.getEdit());
            updateUndoRedoState(); // Update undo/redo menu items' state
        });
    }
 private void updateUndoRedoState() {
	 
 
	 
 }
 private int countWords() {
     String text = textRegion.getText();
     String[] words = text.trim().split("\\s+");
     return words.length;
 }

 

	public void init() {
    	// saved ?
    	boolean save = false;
    	
        menuBar = new JMenuBar();
        fileMenu = new JMenu("File");
        fileoperation1=new JMenu("undo");
        fileoperation2=new JMenu("redo");
        openFileItem = new JMenuItem("Open File");
        insertTemplateItem = new JMenuItem("Insert Report Template"); // Added Insert Template item
        insertTemplateItem2 = new JMenuItem("ARTICLE");
		
        // Add action listener for the Open File item
        openFileItem.addActionListener(this);
        insertTemplateItem.addActionListener(this); // Add action listener for Insert Template item
        insertTemplateItem2.addActionListener(this); // Add action listener for Insert Template item



        // Add components to the menu
        fileMenu.add(openFileItem);
        fileMenu.add(insertTemplateItem); // Add Insert Template item to the File menu
        fileMenu.add(insertTemplateItem2);  // Add Insert Template 2 item to the File menu
        menuBar.add(fileMenu);

        menuBar.add(fileMenu);
        menuBar.add(fileoperation1);
        menuBar.add(fileoperation2);

        

        // Set up file chooser
        fileChooser = new JFileChooser();

        Font font;
        Color color;

        color = colorClass.getColor();
        font = fontClass.getFont();

        // Constructs Components
      
        textRegion = new JTextPane();
        SaveButton = new JButton("Save");
        colorCombo = new JComboBox(colorItems);
        fontCombo = new JComboBox(fontItem);
        processorLabel = new JLabel("Word Processor");
        fontSize = new JSlider(10, 50);
        wordcount=new JLabel("wordcount:");

        // Working with slider
        fontSize.setOrientation(JSlider.HORIZONTAL);
        fontSize.setMinorTickSpacing(1);
        fontSize.setMajorTickSpacing(5);
        fontSize.setPaintTicks(true);
        fontSize.setPaintLabels(true);

        // Make text area look presentable to the user
        textRegion.setBackground(Color.LIGHT_GRAY);

        // Editing size and layout
        setPreferredSize(new Dimension(400, 630));
        setLayout(null);
        // add this in logic most likely if statement
        //JOptionPane.showConfirmDialog("File not saved. Are you sure you want to quit", JOptionPane.INFORMATION_MESSAGE, "File not save", 0);

        //JLabel wordcount=new JLabel("wordcount:");
        
        
        
        
        // Add components
        add(SaveButton);
        add(textRegion);
        add(colorCombo);
        add(fontCombo);
        add(processorLabel);
        add(fontSize);
        add(wordcount);

        // Boundaries
        textRegion.setBounds(150, 10, 1000, 850);
        SaveButton.setBounds(1270, 315, 140, 35);
        colorCombo.setBounds(1270, 205, 140, 53);
        fontCombo.setBounds(1270, 150, 140, 35);
        processorLabel.setBounds(1270, 20, 140, 35);
        fontSize.setBounds(1270, 95, 140, 49);
        wordcount.setBounds(1270,400,90,50);
        menuBar.setBounds(100, 10, 140, 40);

        // Adding action listener
        SaveButton.addActionListener(this);
        colorCombo.addActionListener(this);
        fontCombo.addActionListener(this);

        // confirmation on each tab that is closed or opened 
        JFrame frame = new JFrame("Word Processor");
        frame.setJMenuBar(menuBar);
        frame.add(this);
        frame.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
        frame.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                int option = JOptionPane.showConfirmDialog(frame,
                    "Are you sure you want to close the window?", "Confirm Close",
                    JOptionPane.YES_NO_OPTION);
                
                if (option == JOptionPane.YES_OPTION) {
                    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Allow the window to close
                }
            }
        });
        frame.pack();
        frame.setVisible(true);
        
        
    }

    private static Object split(String string) {
		// TODO Auto-generated method stub
		return null;
	}

	public void actionPerformed(ActionEvent e) {
        if (e.getSource() == SaveButton) {
        	 if (hasUnsavedChanges()) {
                 int response = JOptionPane.showConfirmDialog(this,
                     "You have pressed saved,are you sure you want to continue with this application?",
                     "saving item", JOptionPane.YES_NO_CANCEL_OPTION);
                 if (response == JOptionPane.YES_OPTION) {
                     // Save the file, and allow the user to decide whether to overwrite
                     if (!saveFile.save(textRegion)) {
                         return; // User canceled the save
                     }
                 } else if (response == JOptionPane.CANCEL_OPTION) {
                     return; // User canceled the save operation
                 }
             } else {
                 // No unsaved changes, save directly
                 saveFile.save(textRegion);
             }
        
            
            // Call save class
           
        } if (e.getSource() == openFileItem) {
        	 if (hasUnsavedChanges()) {
                 int response = JOptionPane.showConfirmDialog(this,
                     "You have unsaved changes. Do you want to save them before opening a new file?",
                     "Unsaved Changes", JOptionPane.YES_NO_CANCEL_OPTION);
                 if (response == JOptionPane.YES_OPTION) {
                     // Save the changes, and allow the user to decide whether to overwrite
                     if (!saveFile.save(textRegion)) {
                         return; // User canceled the save operation
                     }
                 } else if (response == JOptionPane.CANCEL_OPTION) {
                     return; // User canceled the operation
                 }
             }

             int returnVal = fileChooser.showOpenDialog(this);
             if (returnVal == JFileChooser.APPROVE_OPTION) {
                 File file = fileChooser.getSelectedFile();
                 // Handle file opening here
                 // You can use the 'file' variable to access the selected file.
                 // Implement your logic for opening and displaying the file's content.
             }
        
  
   
             
            // Open file logic
    } if (e.getSource() == insertTemplateItem) {
            // Insert template logic
            insertTemplate("Dear Sir/Madam\n\n\nYours Sincerely");
        }
     if (e.getSource() == insertTemplateItem2) {
        // Insert template logic
        insertTemplate("Article");
    }
        if (e.getSource() == colorCombo) {
            colorClass.selectColor(colorCombo.getSelectedItem().toString());
            textRegion.setForeground(colorClass.getColor());
            // Call color task
        }
        if (e.getSource() == fontCombo) {
            fontClass.selectFont(fontCombo.getSelectedItem().toString(), fontSize.getValue());
            textRegion.setFont(fontClass.getFont());
            // Call font task
        }
        if (e.getSource() == openFileItem) {
            int returnVal = fileChooser.showOpenDialog(this);

            if (returnVal == JFileChooser.APPROVE_OPTION) {
                File file = fileChooser.getSelectedFile();
                // Handle file opening here
                // You can use the 'file' variable to access the selected file.
                // Implement your logic for opening and displaying the file's content.
            }
            }
        }
        
  
	public JTextPane getText() {
        return textRegion;
    }
    
    // Add a method to insert a template at the current caret position
    private void insertTemplate(String templateText) {
        int caretPosition = textRegion.getCaretPosition();
        try {
            textRegion.getDocument().insertString(caretPosition, templateText, null);
        } catch (BadLocationException e) {
            e.printStackTrace();
        }
    }
    private boolean hasUnsavedChanges() {
        // Implement this method to check if there are unsaved changes in the text editor.
        
        return true; // Replace with your logic
    }


    


    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new Visual();
            
       });
   }
}
        
    
    



