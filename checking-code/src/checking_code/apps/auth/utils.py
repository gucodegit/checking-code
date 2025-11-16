import datetime

import jwt
from fastapi import HTTPException, status
from passlib.context import CryptContext

from checking_code.core.settings import settings


class AuthUtil:
    secret = settings.secret_key.get_secret_value()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def create_access_token(self, user_id: int, user: str) -> str:
        expire = datetime.datetime.now() + datetime.timedelta(
            seconds=settings.access_token_expire
        )
        data = {"exp": expire, "user_id": str(user_id), "user_type": user}
        encoded_jwt = jwt.encode(payload=data, key=self.secret, algorithm="HS256")
        return encoded_jwt

    async def decode_access_token(self, token: str) -> dict:
        try:
            return jwt.decode(jwt=token, key=self.secret, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired"
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
            )
