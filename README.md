🎤 VoiceBot – Intelligent Voice Assistant
AI Intern Project • Complete End-to-End Speech Interaction System

This project implements a fully functional voice-based AI assistant capable of:

Speech-to-Text (STT)

Intent Detection (NLU)

Response Generation

Text-to-Speech (TTS)

Backend + Database Integration

The bot accepts voice input, understands the meaning, fetches data from a database, generates a reply, and speaks the answer back.

🚀 Features Implemented
✔ 1. Speech-to-Text

Technology: Vosk Offline Speech Recognition

Accepts microphone input & uploaded audio

Converts speech → text without internet

✔ 2. Natural Language Understanding (NLU)

A hybrid system:

Rule-based intent detection

Machine Learning fallback using HuggingFace (distilbert-base-uncased-emotion)

Additional FAQ intent detection (regex-based)

Understands intents like:

Working hours

Services offered

Reset password

Contact info

Greetings

Positive & negative expressions

✔ 3. Response Generation

Rule-based response engine

Database-backed FAQs

Personalized answers based on detected intent

✔ 4. Text-to-Speech (TTS)

Technology: pyttsx3 (offline TTS engine)

Converts generated reply → WAV audio bytes

API returns audio so frontend/test script can play it

✔ 5. Backend + Database Integration

Backend Framework: FastAPI
Database: MySQL

A faq table stores:
| intent             | answer                              |
| ------------------ | ----------------------------------- |
| faq_working_hours  | Our working hours are 9 AM to 6 PM… |
| faq_services       | We offer customer support…          |
| faq_contact        | You can contact us at…              |
| faq_location       | We are located at…                  |
| faq_reset_password | To reset your password…             |
Bot responds from the database dynamically.

voicebot/
│
├── backend/
│   └── api.py
│
├── speech_to_text/
│   ├── stt.py
│   └── vosk-model-small-en-us-0.15/   (ignored in Git)
│
├── nlu/
│   ├── intent_classifier.py
│   └── faq_intents.py
│
├── response_engine/
│   └── response_generator.py
│
├── tts/
│   └── text_to_speech.py
│
├── test_voicebot.py
├── main.py
├── requirements.txt
└── README.md

<img width="518" height="586" alt="image" src="https://github.com/user-attachments/assets/db34ace2-5fe8-4719-b000-0d6732581aec" />


🗄️ MySQL Setup

Create database:
CREATE DATABASE voicebot;
USE voicebot;


Create FAQ table:
CREATE TABLE faq (
    intent VARCHAR(50) PRIMARY KEY,
    answer TEXT
);


Insert sample data:
INSERT INTO faq VALUES
("faq_working_hours", "Our working hours are 9 AM to 6 PM, Monday to Saturday."),
("faq_contact", "You can contact support at: support@example.com"),
("faq_location", "We are located in Pune, Maharashtra."),
("faq_services", "We offer customer support, inquiry handling, and account services."),
("faq_reset_password", "To reset your password, visit the profile section and choose reset.");

⚡ Running the Backend
Start the server:
uvicorn main:app --reload

Backend will run at:
http://127.0.0.1:8000


Swagger docs:
http://127.0.0.1:8000/docs


🧪 Testing Voice Interaction

Run the test script:
python test_voicebot.py

Flow:
Mic records 3 seconds of audio
File is sent to /voicebot/audio
Backend performs:
    STT
    Intent detection
    Database lookup
    Response generation
    TTS
Audio reply is played automatically


🔥 End-to-End Pipeline Diagram
Voice Input → STT (Vosk) → NLU (Rules + Transformer)
        ↓
   Intent Detected
        ↓
Database Lookup (MySQL)
        ↓
Response Generated
        ↓
TTS (pyttsx3)
        ↓
Voice Output


📌 API Endpoints
POST /nlu

Send text → get intent
{ "text": "What services do you offer?" }

POST /respond

Send text → get intent + reply
{ "intent": "faq_services", "reply": "We offer…" }

POST /voicebot/audio

Send audio → receive audio reply (WAV)

⭐ Extra 
Hybrid NLU (rules + ML)
Offline STT + Offline TTS
Professional architecture
Modular folder-based design
Real-time full voice pipeline
Intent + database integration



👨‍💻 Author
Shreyash
