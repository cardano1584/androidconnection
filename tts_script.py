# Import necessary modules
from gtts import gTTS
import os
import subprocess

# Function to get clipboard content using Termux
def get_clipboard_content():
    try:
        # Run the Termux clipboard-get command
        result = subprocess.check_output(["termux-clipboard-get"]).decode("utf-8")
        return result.strip()
    except subprocess.CalledProcessError:
        return None

# Get clipboard content
clipboard_text = get_clipboard_content()

# Check if clipboard content is available
if clipboard_text:
    # Create a gTTS object with the clipboard content
    tts = gTTS(clipboard_text, lang='en')

    # Save the speech as an audio file (e.g., tts_output.mp3)
    tts.save("tts_output.mp3")

    # Play the audio using Termux's built-in media player (mpv)
    os.system("termux-media-player play tts_output.mp3")

else:
    print("Clipboard is empty. Nothing to convert to speech.")
