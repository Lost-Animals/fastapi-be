import os

from dotenv import load_dotenv

load_dotenv()

SA_KEY_PATH = os.environ.get("SA_KEY_PATH")
DATABASE_NAME = os.environ["DATABASE_NAME"]
JWT_KEY = os.environ["JWT_KEY"]

GOOGLE_CLIENT_ID = os.environ["GOOGLE_CLIENT_ID"]
GOOGLE_CLIENT_SECRET = os.environ["GOOGLE_CLIENT_SECRET"]
GOOGLE_CALLBACK_URL = os.environ.get(
    "GOOGLE_CALLBACK_URL", "http://localhost:8000/auth/callback"
)

IS_DEV = bool(os.environ.get("IS_DEV", False))

STORAGE_SERVICE_URL = os.environ["STORAGE_SERVICE_URL"]
