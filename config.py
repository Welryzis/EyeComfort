import os
from dotenv import load_dotenv

load_dotenv()


TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")
TG_MESSAGE = "Time ;)"

FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
