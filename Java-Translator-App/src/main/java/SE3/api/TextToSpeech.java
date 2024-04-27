package SE3.api;

import com.sun.speech.freetts.Voice;
import com.sun.speech.freetts.VoiceManager;

public class TextToSpeech {
	//The voice that will produce the speech
	private Voice voice;
	
	/**
	 * Creates the voice that is going to be used in the speech
	 */
    public TextToSpeech() {
    	VoiceManager voiceManager = VoiceManager.getInstance();
    	voice = voiceManager.getVoice("kevin16");
    }

    /**
     * Converts the given text into speech that is then played on the device
     * @param text String to be spoken
     * @return false if the voice is null, true if spoken successfully
     */
    public boolean speak(String text) {
    	if (voice == null) {
    		//If voice is null try setting it again
    		voice = VoiceManager.getInstance().getVoice("kevin16");
    		//If voice is still null give up, return false
    		if (voice == null) return false;
    	}
    	
    	//Set the voice as the current speaker and read the text aloud
        voice.allocate();
        voice.speak(text);
        return true;
    }
}
