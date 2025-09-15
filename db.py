from google.cloud.firestore import AsyncClient


from config import DATABASE_NAME, IS_DEV


def create_db():
    if IS_DEV:
        from google_sa import credentials

        return AsyncClient(credentials=credentials, database=DATABASE_NAME)

    return AsyncClient(database=DATABASE_NAME)


db = create_db()
