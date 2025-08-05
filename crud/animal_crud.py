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
        pass

    return Animal(id=doc.id, **animal_dict)
