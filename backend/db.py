# backend/db.py

from sqlalchemy import create_engine, text

# Change these if your MySQL username/password differ
DB_USER = "root"
DB_PASSWORD = "LeBronJames_23"   
DB_HOST = "localhost"
DB_NAME = "voicebot"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

def get_faq_answer(intent: str):
    query = text("SELECT answer FROM faqs WHERE intent = :intent LIMIT 1")
    with engine.connect() as conn:
        result = conn.execute(query, {"intent": intent}).fetchone()

    if result:
        return result[0]
    else:
        return "Sorry, I don't have an answer for that question."
