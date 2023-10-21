# Import the gTTS library
from gtts import gTTS
import os

# Input text to be converted to speech
text_to_speech = "Hello, this is a text-to-speech demonstration in Termux."

# Create a gTTS object
tts = gTTS(text_to_speech, lang='en')

# Save the speech as an audio file (e.g., tts_output.mp3)
tts.save("tts_output.mp3")

# Play the audio using Termux's built-in media player (mpv)
os.system("termux-media-player play tts_output.mp3")
