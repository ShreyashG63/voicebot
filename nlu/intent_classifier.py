import re
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# ---------------------- FAQ INTENT DETECTOR ------------------------
def detect_faq_intent(text: str):
    text = text.lower()

    # Working hours
    if re.search(r"hour|open|close|timing|time you|when do you", text):
        return "faq_working_hours"

    # Contact support
    if re.search(r"contact|support|email|help", text):
        return "faq_contact"

    # Location
    if re.search(r"located|address|where are you|location", text):
        return "faq_location"

    # Services
    if re.search(r"service|offer|provide|what do you do", text):
        return "faq_services"

    # Reset password
    if re.search(r"password|reset|forgot", text):
        return "faq_reset_password"

    return None


# ---------------------- LOAD ML MODEL -------------------------------
MODEL_NAME = "bhadresh-savani/distilbert-base-uncased-emotion"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

# ---------------------- EXTRA RULE-BASED INTENTS --------------------
INTENT_KEYWORDS = {
    "check_balance": ["balance", "account balance", "bank balance"],
    "greeting": ["hello", "hi", "hey"],
    "goodbye": ["bye", "goodbye", "see you"]
}


# ---------------------- FINAL INTENT CLASSIFIER ---------------------
def classify_intent(text):
    text = text.lower()

    # 1️⃣ Check FAQ intents first
    faq_intent = detect_faq_intent(text)
    if faq_intent:
        return faq_intent

    # 2️⃣ Check rule-based intents
    for intent, keywords in INTENT_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            return intent

    # 3️⃣ ML model fallback
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    probs = F.softmax(logits, dim=1)
    predicted_class = torch.argmax(probs).item()

    # 4️⃣ Convert emotion categories → generic intents
    if predicted_class in [0, 1, 2]:   # sadness / joy / love
        return "general_positive"

    elif predicted_class in [3, 4]:    # anger / fear
        return "general_negative"

    else:
        return "unknown_intent"
