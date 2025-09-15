from fastapi import APIRouter

from routers import animal_router, auth_router


main_router = APIRouter()
main_router.include_router(animal_router.router)
main_router.include_router(auth_router.router)
