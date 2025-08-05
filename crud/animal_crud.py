from google.cloud.exceptions import NotFound

from db import db
from schemas.animal_schemas import Animal, AnimalData


animals_ref = db.collection("animals")


async def insert_animal(data: AnimalData) -> Animal:
    animal_data_dict = data.model_dump()
    new_animal_ref = animals_ref.document()
    await new_animal_ref.set(animal_data_dict)
    new_animal = Animal(id=new_animal_ref.id, **animal_data_dict)
    return new_animal


async def select_animal_by_id(id: str) -> Animal:
    doc_ref = animals_ref.document(id)
    doc = await doc_ref.get()
    animal_dict = doc.to_dict()
    if not animal_dict:
        raise NotFound("No animal found with that id!")

    return Animal(id=doc.id, **animal_dict)


async def update_animal(animal_id: str, data: AnimalData) -> Animal:
    doc_ref = animals_ref.document(animal_id)
    doc = await doc_ref.get()

    if not doc.exists:
        raise NotFound("No animal found with that id!")

    updated_data = data.model_dump()
    await doc_ref.update(updated_data)

    return Animal(id=animal_id, **updated_data)


async def delete_animal(animal_id: str) -> None:
    doc_ref = animals_ref.document(animal_id)
    doc = await doc_ref.get()

    if not doc.exists:
        raise NotFound("No animal found with that id!")

    await doc_ref.delete()
