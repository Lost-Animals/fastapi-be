from httpx import AsyncClient, HTTPStatusError

from config import STORAGE_SERVICE_URL
from schemas.image_schemas import Image
from utils.custom_exceptions import StorageServiceError


async def upload_image(image_base64_data: str) -> Image:
    """
    Upload an image to the storage service.

    Args:
        image_base64_data (str): The image data encoded as a base64 string.

    Returns:
        Image: The uploaded image metadata parsed into an Image schema.

    Raises:
        StorageServiceError: If the storage service returns an error response.
    """
    async with AsyncClient(base_url=STORAGE_SERVICE_URL) as client:
        try:
            resp = await client.post(
                "/images",
                json={"image_base64": image_base64_data},
                timeout=30.0,
            )
            resp.raise_for_status()
            return Image(**resp.json())
        except HTTPStatusError as e:
            raise StorageServiceError(e.response.status_code, e.response.text)


async def get_image_url(image_name: str) -> str:
    """
    Retrieve the URL of an image from the storage service.

    Args:
        image_name (str): The name of the image to retrieve.

    Returns:
        str: The public URL of the image.

    Raises:
        StorageServiceError: If the storage service returns an error response.
    """
    async with AsyncClient(base_url=STORAGE_SERVICE_URL) as client:
        try:
            resp = await client.get(f"/images/{image_name}", timeout=10.0)
            resp.raise_for_status()
            data = resp.json()
            return data.get("url")
        except HTTPStatusError as e:
            raise StorageServiceError(e.response.status_code, e.response.text)


async def delete_image(image_name: str) -> str:
    """
    Delete an image from the storage service.

    Args:
        image_name (str): The name of the image to delete.

    Returns:
        str: Confirmation message from the storage service.

    Raises:
        StorageServiceError: If the storage service returns an error response.
    """
    async with AsyncClient(base_url=STORAGE_SERVICE_URL) as client:
        try:
            resp = await client.delete(f"/images/{image_name}", timeout=10.0)
            resp.raise_for_status()
            data = resp.json()
            return data.get("message", "Image deleted")
        except HTTPStatusError as e:
            raise StorageServiceError(e.response.status_code, e.response.text)
