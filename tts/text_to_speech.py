import pyttsx3
from io import BytesIO
import os
import uuid

engine = pyttsx3.init()

def tts_to_bytes(text: str):
    temp_filename = f"temp_tts_{uuid.uuid4().hex}.wav"

    # Save TTS to temporary WAV file
    engine.save_to_file(text, temp_filename)
    engine.runAndWait()

    # Load it into memory as bytes
    with open(temp_filename, "rb") as f:
        audio_bytes = f.read()

    # Remove temp file
    os.remove(temp_filename)

    return audio_bytes
