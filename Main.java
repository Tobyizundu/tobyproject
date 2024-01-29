import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import javax.swing.JFrame;



public class Main {
	
	    public static void main(String args[]){
	       JFrame display =new JFrame("WORD PROCESSOR");
	       display.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	       display.getContentPane().add(new Visual());
	       display.pack();
	       display.setVisible(true);
	     

	    }


}
