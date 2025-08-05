from google.cloud.firestore import AsyncClient

from google_sa import credentials
from config import DATABASE_NAME

db = AsyncClient(credentials=credentials, database=DATABASE_NAME)
