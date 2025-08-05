from fastapi import APIRouter, status, HTTPException
from google.cloud.exceptions import NotFound

from schemas.animal_schemas import Animal, AnimalData
from crud.animal_crud import (
    insert_animal,
    select_animal_by_id,
    update_animal,
    delete_animal,
)


router = APIRouter(prefix="/animals", tags=["Animals"])


@router.post("/", response_model=Animal, status_code=status.HTTP_201_CREATED)
async def post_animal(data: AnimalData):
    animal = await insert_animal(data)
    return animal


@router.get("/{animal_id}", response_model=Animal)
async def get_animal_by_id(animal_id: str):
    try:
        animal = await select_animal_by_id(animal_id)
    except NotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)

    return animal


@router.put("/{animal_id}", response_model=Animal)
async def put_animal(animal_id: str, data: AnimalData):
    try:
        updated_animal = await update_animal(animal_id, data)
    except NotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)

    return updated_animal


@router.delete("/{animal_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_animal_by_id(animal_id: str):
    try:
        await delete_animal(animal_id)
    except NotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)

    return "OK"
