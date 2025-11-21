def generate_response(intent):
    responses = {
        "greeting": "Hello! How can I assist you today?",
        "check_balance": "Sure, I can help you with your account balance. Please wait while I fetch the details.",
        "reset_password": "No problem! I can help you reset your password. Please follow the instructions sent to your email.",
        "services": "We provide a variety of customer services including account management, password help, and support.",
        "goodbye": "Goodbye! Have a great day.",
        "general_positive": "I'm glad to hear that! How can I help you more?",
        "general_negative": "I'm sorry to hear that. Could you please tell me what went wrong?",
        "unknown_intent": "I'm not sure I understood that. Could you please rephrase your question?"
    }

    return responses.get(intent, "Sorry, I didn't understand that. Can you repeat?")
