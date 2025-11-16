from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.requests import Request

from checking_code.apps.auth.utils import AuthUtil
from checking_code.apps.auth.schemas import GetAuthSchema


async def get_token_from_cookies(request: Request) -> str:
    token = request.cookies.get("Authorization")
    if not (token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is missing"
        )
    return token


async def get_current_user(
    token: Annotated[str, Depends(get_token_from_cookies)],
    util: AuthUtil = Depends(AuthUtil),
) -> GetAuthSchema:
    decoded_token = await util.decode_access_token(token=token)
    return GetAuthSchema(
        id=int(decoded_token["user_id"]), user_type=decoded_token["user_type"]
    )
