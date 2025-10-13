import java.awt.Font;

public class FontSetting {
	Font font;

	  public void selectFont(String selection,int size){
	        if(selection.equals("Arial")){          
	            font=new Font("Arial",Font.PLAIN,size);
	            
	           
	            

	        }if(selection.equals("New time roman")){
	        font=new Font("New_time_roman",Font.PLAIN,size);
	        
	      
	        
	        }if(selection.equals("Monospaced")){
	        font=new Font("Monospaced",Font.PLAIN,size);      
	        
	        }if(selection.equals("Serif")){
	        font=new Font("SERIF",Font.PLAIN,size);
	        
	        }if(selection.equals("Sans serif")){
	        font=new Font("SANS_SERIF",Font.PLAIN,size);
	        }
	  }
	    
	    
		public Font getFont(){

	        return font;
	    }
	}
