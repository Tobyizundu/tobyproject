package SE3;

import SE3.api.TextToSpeech;
import SE3.gui.AppGUI;

public class Main {
    public static void main(String[] args) {
    	//Set the system property allowing access to TTS voices
    	System.setProperty("freetts.voices", "com.sun.speech.freetts.en.us.cmu_us_kal.KevinVoiceDirectory");
        //Create the GUI
    	new AppGUI();
        //test
    }
}