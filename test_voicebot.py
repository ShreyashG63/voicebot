import sounddevice as sd
import soundfile as sf
from io import BytesIO
import requests

# Record audio
fs = 16000
duration = 3   # seconds
print("Speak now...")
audio = sd.rec(
    int(duration * fs),
    samplerate=fs,
    channels=1,
    device=1
)
sd.wait()

# Save temporary user audio
sf.write("user.wav", audio, fs)

# Send to backend
with open("user.wav", "rb") as f:
    resp = requests.post(
        "http://127.0.0.1:8000/voicebot/audio",
        files={"file": ("user.wav", f, "audio/wav")}
    )

# Play backend audio
audio_bytes = resp.content
data, samplerate = sf.read(BytesIO(audio_bytes))
sd.play(data, samplerate)
sd.wait()
