from fastapi import APIRouter, status

from schemas.animal_schemas import Animal, AnimalData
from crud.animal_crud import insert_animal, select_animal_by_id


router = APIRouter(prefix="/animals", tags=["Animals"])


@router.post("/", response_model=Animal, status_code=status.HTTP_201_CREATED)
async def post_animal(data: AnimalData):
    animal = await insert_animal(data)
    return animal


@router.get("/{animal_id}", response_model=Animal)
async def get_animal_by_id(animal_id: str):
    animal = await select_animal_by_id(animal_id)
    return animal
