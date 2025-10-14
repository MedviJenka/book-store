import jwt
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Union, Any
from uuid import uuid4
from backend.settings import Config
from backend.utils.logs import Logfire
from backend.database.schemas import UserAccessSchema

log = Logfire(name="token-session")


@dataclass
class TokenManager:

    user_schema: UserAccessSchema
    expire: Union[int, timedelta] = 3600  # seconds
    refresh: bool = False

    def create_access_token(self) -> str:
        payload = {
            "id": str(uuid4()),
            "email": self.user_schema.email,
            "exp": datetime.now() + timedelta(seconds=self.expire),
            "refresh": self.refresh
        }

        token = jwt.encode(payload, key=Config.SUPABASE_JWT_TOKEN, algorithm=Config.ALGORITHM)
        log.fire.info("Token created successfully")
        return token

    @staticmethod
    def decode_token(token: str) -> Any:
        try:
            data = jwt.decode(jwt=token, key=Config.SUPABASE_JWT_TOKEN, algorithms=[Config.ALGORITHM])
            log.fire.info(f"Decoded token: {data}")
            return data
        except jwt.ExpiredSignatureError:
            log.fire.error("Token expired")
        except jwt.InvalidTokenError:
            log.fire.error("Invalid token")
        return None
