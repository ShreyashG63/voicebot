from speech_to_text.stt import listen_and_transcribe
from nlu.intent_classifier import classify_intent
from response_engine.response_generator import generate_response
from tts.text_to_speech import speak_text

print("🎤 Voice Bot Ready!")
print("Say something whenever you're ready.\n")

while True:
    print("Listening...")
    text = listen_and_transcribe()

    if not text:
        print("Didn't catch that. Try again.")
        continue

    print("You said:", text)

    intent = classify_intent(text)
    print("Detected Intent:", intent)

    response = generate_response(intent)
    print("Bot:", response)

    speak_text(response)

    if intent == "goodbye":
        break
