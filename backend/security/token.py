from typing import Optional
from fastapi import Request
from backend.utils.logs import Logfire
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


log = Logfire(name='token-engine')


class AccessTokenBearer(HTTPBearer):

    def __init__(self, auto_error) -> None:
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]:
        cred = await super().__call__(request=request)
        log.fire.info(cred.scheme)
        log.fire.info(cred.credentials)
