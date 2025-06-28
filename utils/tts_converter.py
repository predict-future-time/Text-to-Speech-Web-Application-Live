from gtts import gTTS

# Convert given text to speech and save as MP3
def convert_text_to_audio(text, output_path, lang='en'):
    tts = gTTS(text, lang=lang)
    tts.save(output_path)
