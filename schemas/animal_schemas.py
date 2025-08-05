from typing import Optional

from pydantic import BaseModel, Field

from utils.enums import AnimalStatusEnum


class BaseAnimal(BaseModel):
    name: str = Field(
        ..., min_length=2, max_length=255, description="The name of the animal"
    )
    microchip: Optional[str] = Field(
        None, max_length=255, description="The microchip of the animal"
    )
    passport_id: Optional[str] = Field(
        None, max_length=255, description="The passport_id of the animal"
    )
    status: AnimalStatusEnum = Field(
        default=AnimalStatusEnum.lost,
        description="The status of the animal - lost, found.",
    )


class AnimalData(BaseAnimal):
    pass


class Animal(BaseAnimal):
    id: str
