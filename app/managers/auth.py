## Authorioze Users
from datetime import datetime, timedelta
from typing import Optional

from decouple import config
import jwt
from fastapi import HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# from jwt import ExpiredSignatureError, InvalidTokenError
from starlette.requests import Request
from app.db.database import database
from app.models import RoleType
from app.config import settings


class AuthManager:
    @staticmethod
    def encode_token(user):
        try:
            to_encode = {"sub": user["id"], "exp":  datetime.utcnow() + timedelta(minutes=120)}
            return jwt.encode(to_encode, settings.secrest_jwt, algorithm='HS256')
        except Exception as e:
            raise e


class CustomHTTPBearer(HTTPBearer):
    async def __call__(
            self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]:
        res = await super().__call__(request)
        from app.models import user
        try:
            payload = jwt.decode(res.credentials, settings.secrest_jwt, algorithms=['HS256'])
            user = await database.fetch_one(user.select().where(user.c.id == payload["sub"]))
            request.state.user = user
            return user
        except :
            raise HTTPException(401, "Invalid token.")
        # except InvalidTokenError:
        #     raise HTTPException(401, "Invalid token.")

def is_anonymous_user(request: Request):
    if not request.state.user["role"] == RoleType.anonymous_user:
        raise HTTPException(status_code=403, detail="Forbidden")

def is_admin(request: Request):
    if not request.state.user["role"] == RoleType.admin:
        raise HTTPException(status_code=403, detail="Forbidden")

def is_super_admin(request: Request):
    if not request.state.user["role"] == RoleType.super_admin:
        raise HTTPException(status_code=403, detail="Forbidden")
        



oauth2_scheme = CustomHTTPBearer()
