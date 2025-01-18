from config import ROOT_DIR
from gtts import gTTS
import os

class TTS:
    def __init__(self):
        # Initialize the TTS class  
        self.gtts = gTTS
    
    def synthesize(self, text: str, output_file: str = os.path.join(ROOT_DIR, ".mp", "audio.wav")) -> str:
        """
        Synthesizes the given text into speech.

        Args:
            text (str): The text to synthesize.
            output_file (str, optional): The output file to save the synthesized speech. Defaults to "audio.wav".

        Returns:
            str: The path to the output file.
        """
        # Synthesize the text
        tts = self.gtts(text=text, lang='en', tld='co.uk')
        tts.save(output_file)
        return output_file