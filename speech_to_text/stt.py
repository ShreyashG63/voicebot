import sounddevice as sd
import vosk
import json
import queue
import wave
from vosk import Model, KaldiRecognizer

# Load Vosk model
model = Model("speech_to_text/vosk-model-small-en-us-0.15")

# Audio queue
audio_queue = queue.Queue()


def audio_callback(indata, frames, time, status):
    audio_queue.put(bytes(indata))


def listen_and_transcribe():
    sample_rate = 16000
    rec = KaldiRecognizer(model, sample_rate)

    print("🎤 Recording... Speak now!")

    with sd.RawInputStream(samplerate=sample_rate, blocksize=8000,
                           dtype='int16', channels=1, callback=audio_callback):

        while True:
            data = audio_queue.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                print("📝 You said:", text)
                return text


def transcribe_audio_file(file_path):
    wf = wave.open(file_path, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())

    text = ""

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text += " " + result.get("text", "")

    final = json.loads(rec.FinalResult())
    text += " " + final.get("text", "")

    wf.close()
    return text.strip()
