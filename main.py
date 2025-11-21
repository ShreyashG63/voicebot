import uvicorn
from backend.api import app
from speech_to_text.stt import listen_and_transcribe

if __name__ == "__main__":
    print("🚀 Starting Voice Bot backend...")

    # TEST: Try STT once before starting server
    print("Say something after the beep...")
    text = listen_and_transcribe()
    print("You said:", text)

    uvicorn.run(app, host="127.0.0.1", port=8000)
