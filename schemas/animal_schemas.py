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
    location: Optional[str] = Field(
        None, max_length=255, description="The location where was the animal last seen."
    )
    description: Optional[str] = Field(
        None, max_length=255, description="Relevant description about the animal."
    )
    case_date: str = Field(
        ..., max_length=100, description="The date when the animal was lost or found."
    )
    contact_information: str = Field(
        ..., max_length=255, description="Any contact information."
    )


class AnimalData(BaseAnimal):
    pass


class Animal(BaseAnimal):
    id: str
    user_id: str
