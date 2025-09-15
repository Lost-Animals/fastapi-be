from typing import Optional

from google.cloud.exceptions import NotFound

from db import db
from schemas.user_schemas import User, UserCreate


users_ref = db.collection("users")


async def insert_user(data: UserCreate) -> User:
    user_data_dict = data.model_dump()
    new_user_ref = users_ref.document()
    await new_user_ref.set(user_data_dict)
    new_user = User(id=new_user_ref.id, **user_data_dict)
    return new_user


async def select_user_by_email(email: str) -> Optional[User]:
    query = users_ref.where("email", "==", email).limit(1)
    docs = [doc async for doc in query.stream()]

    if not docs:
        return None

    doc = docs[0]
    user_data = doc.to_dict()
    return User(id=doc.id, **user_data)


async def select_user_by_id(user_id: str) -> User:
    doc_ref = users_ref.document(user_id)
    doc = await doc_ref.get()

    if not doc.exists:
        raise NotFound(f"User with id '{user_id}' not found.")

    data = doc.to_dict()
    return User(id=doc.id, **data)
