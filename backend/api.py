# backend/api.py

from fastapi import FastAPI
from pydantic import BaseModel

from nlu.intent_classifier import classify_intent
from response_engine.response_generator import generate_response
from tts.text_to_speech import tts_to_bytes
from speech_to_text.stt import transcribe_audio_file

from backend.db import get_faq_answer   # << NEW

from fastapi import UploadFile, File
from fastapi.responses import StreamingResponse
from io import BytesIO

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Voice bot backend is running!"}


class TextInput(BaseModel):
    text: str


# --------------------- TEXT TO INTENT ----------------------------
@app.post("/nlu")
def detect_intent(data: TextInput):
    intent = classify_intent(data.text)
    return {"intent": intent}


# ------------------- TEXT TO RESPONSE (NO DB) ---------------------
@app.post("/respond")
def generate_bot_reply(data: TextInput):
    intent = classify_intent(data.text)

    # If it’s an FAQ → get answer from database
    if intent.startswith("faq_"):
        reply = get_faq_answer(intent)
    else:
        reply = generate_response(intent)

    return {
        "intent": intent,
        "reply": reply
    }


# ------------------- FULL VOICE → BOT → VOICE ---------------------
@app.post("/voicebot/audio")
async def voicebot_audio(file: UploadFile = File(...)):

    # 1. Save uploaded file
    temp_input = "temp_input.wav"
    with open(temp_input, "wb") as f:
        f.write(await file.read())

    # 2. Speech-to-Text
    text = transcribe_audio_file(temp_input)

    # 3. NLU
    intent = classify_intent(text)

    # 4. DB or rule-based response
    if intent.startswith("faq_"):
        reply = get_faq_answer(intent)
    else:
        reply = generate_response(intent)

    # 5. TTS → audio bytes
    audio_bytes = tts_to_bytes(reply)

    # 6. Return audio
    return StreamingResponse(
        BytesIO(audio_bytes),
        media_type="audio/wav"
    )
