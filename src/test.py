from gtts import gTTS
import os

def synthesize_text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='en', tld='co.uk')
    tts.save(output_file)
    return output_file

if __name__ == '__main__':
    test_text = "Looking for a Free Text to Speech API? We got you. See how you can save by trying the best free TTS."
    output_wav_file = os.path.join(os.getcwd(), "test_audio.wav")
    synthesize_text_to_speech(test_text, output_wav_file)
    print(f"Synthesized speech saved to: {output_wav_file}")