from google.cloud.exceptions import NotFound
from google.cloud.firestore import FieldFilter

from db import db
from schemas.image_schemas import DbImage, DbImageCreate


images_ref = db.collection("images")


async def insert_image(data: DbImageCreate) -> DbImage:
    image_data_dict = data.model_dump()
    new_image_ref = images_ref.document()
    await new_image_ref.set(image_data_dict)

    return DbImage(id=new_image_ref.id, **image_data_dict)


async def select_images_by_animal_id(animal_id: str) -> list[DbImage]:
    query = images_ref.where("animal_id", "==", animal_id)
    docs = await query.get()

    # if not docs:
    #     raise NotFound(f"No images found for animal_id={animal_id}")

    return [DbImage(id=doc.id, **doc.to_dict()) for doc in docs]


async def delete_image(image_id: str) -> None:
    doc_ref = images_ref.document(image_id)
    doc = await doc_ref.get()

    if not doc.exists:
        raise NotFound("No image found with that id!")

    await doc_ref.delete()


async def delete_image_by_name(image_name: str) -> None:
    image_filter = FieldFilter("name", "==", image_name)

    query = images_ref.where(filter=image_filter)
    docs = query.stream()

    async for doc in docs:
        await doc.reference.delete()
