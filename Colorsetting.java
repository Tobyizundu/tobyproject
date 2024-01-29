import java.awt.Color;

public class Colorsetting {
	  Color color;
	    public void selectColor(String selection){
	        if(selection.equals("Red")){   //giving text color red 
	            color=Color.RED;
	            
	        } if(selection.equals("Blue")){    //giving text color blue 
	            color=Color.BLUE;

	        }if(selection.equals("Green")){    //giving text color green 
	            color=Color.GREEN;

	        }if(selection.equals("Black")){   //giving text color black
	            color=Color.BLACK;


	    }
	}
	    public Color getColor(){
	        return color;
	    }
	}



