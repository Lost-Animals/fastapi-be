from fastapi import APIRouter, Depends, status, HTTPException
from google.cloud.exceptions import NotFound

from schemas.image_schemas import ImageCreate, Image, ImageRequest
from utils.storage import upload_image, get_image_url, delete_image as storage_delete_image
from crud.image_crud import insert_image, select_images_by_animal_id, delete_image_by_name
from auth.token import verify_token

router = APIRouter(prefix="/images", tags=["Images"])

# TODO check is the image for an animal which is for the same user

@router.post(
    "/",
    response_model=Image,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(verify_token)]
)
async def post_animal_image(data: ImageRequest):
    """
    Upload an image to storage and save it in Firestore.
    """
    uploaded_image = await upload_image(data.base64_data)
    await insert_image(ImageCreate(
        animal_id=data.animal_id,
        name=uploaded_image.name
    ))

    return uploaded_image


@router.get(
    "/animal/{animal_id}",
    response_model=list[Image],
    dependencies=[Depends(verify_token)]
)
async def get_animal_images(animal_id: str):
    """
    Retrieve all images for a specific animal.
    """
    animal_images = await select_images_by_animal_id(animal_id)
    images = [Image(name=image.name, url=await get_image_url(image.name)) for image in animal_images]
    return images
    

@router.delete(
    "/{image_name}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(verify_token)]
)
async def delete_image(image_name: str):
    """
    Delete an image by its name.
    """
    try:
        await storage_delete_image(image_name)
        await delete_image_by_name(image_name)
    except NotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
