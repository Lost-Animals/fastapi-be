from pydantic import BaseModel


class ImageCreate(BaseModel):
    name: str
    animal_id: str


class ImageRequest(BaseModel):
    base64_data: str
    animal_id: str


class AnimalImage(BaseModel):
    name: str
    id: str
    animal_id: str


class Image(BaseModel):
    name: str
    url: str