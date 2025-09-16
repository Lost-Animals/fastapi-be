from pydantic import BaseModel


class StorageImageCreate(BaseModel):
    base64_data: str

class StorageImage(BaseModel):
    name: str
    url: str


class DbImageCreate(BaseModel):
    name: str
    animal_id: str


class DbImage(BaseModel):
    name: str
    id: str
    animal_id: str


class ImageRequest(BaseModel):
    base64_data: str
    animal_id: str


class ImageResp(BaseModel):
    id: str
    name: str
    url: str
    animal_id: str
