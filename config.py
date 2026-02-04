import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ---------------- PLIVO CREDENTIALS ----------------
AUTH_ID = os.getenv("PLIVO_AUTH_ID", "YOUR_AUTH_ID")
AUTH_TOKEN = os.getenv("PLIVO_AUTH_TOKEN", "YOUR_AUTH_TOKEN")

# ---------------- PHONE NUMBERS ----------------
SOURCE_NUMBER = os.getenv("PLIVO_PHONE_NUMBER", "YOUR_PLIVO_NUMBER")
ASSOCIATE_NUMBER = os.getenv("ASSOCIATE_NUMBER", "PLACEHOLDER_NUMBER")

# ---------------- SERVER URL ----------------
BASE_URL = os.getenv("BASE_URL", "https://your-ngrok-url.ngrok.io")
