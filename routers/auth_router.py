from fastapi import APIRouter, Request, status, Depends
from fastapi.responses import RedirectResponse

from auth.google_auth import google_sso
from schemas.user_schemas import UserCreate
from auth.token import create_access_token, get_current_user_id, create_refresh_token
from crud.user_crud import select_user_by_email, insert_user, select_user_by_id


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.get("/login", tags=["Google SSO"])
async def google_login(return_url: str):
    async with google_sso:
        return await google_sso.get_login_url(state=return_url)


@router.get("/callback", tags=["Google SSO"])
async def google_callback(request: Request):
    async with google_sso:
        user = await google_sso.verify_and_process(request)
        return_url = google_sso.state

    if not user:
        return RedirectResponse(
            url=f"{return_url}?error=Invalid%20user",
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    user_stored = await select_user_by_email(user.email)
    if not user_stored:
        user_to_add = UserCreate(
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
        )
        user_stored = await insert_user(user_to_add)
    access_token = create_access_token(user_stored)
    refresh_token = create_refresh_token(user_stored)
    response = RedirectResponse(
        url=f"{return_url}?access_token={access_token}&refresh_token={refresh_token}",
        status_code=status.HTTP_302_FOUND,
    )
    return response


@router.get("/refresh", tags=["Refresh tokens"])
async def refresh_tokens(
    user_id: str = Depends(get_current_user_id)
):
    user = await select_user_by_id(user_id)
    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)
    resp = {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }
    return resp
