from typing import Optional
from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from backend.security.token_manager import TokenManager
from backend.utils.logs import Logfire
from backend.database.schemas import UserAccessSchema


log = Logfire(name="token-engine")


class AccessTokenBearer(HTTPBearer):

    def __init__(self, auto_error: bool = True) -> None:
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]:
        credentials = await super().__call__(request)
        if credentials:
            log.fire.info(f"Scheme: {credentials.scheme}")
            log.fire.info(f"Credentials: {credentials.credentials}")
            return credentials
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authorization")

    @staticmethod
    def validate_token(token: str, email: str) -> bool:
        token_manager = TokenManager(user_schema=UserAccessSchema(email=email))
        token_data = token_manager.decode_token(token)
        return token_data is not None
