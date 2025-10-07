from typing import Union

import jwt
from uuid import uuid4
from datetime import timedelta, datetime
from backend.settings import Config
from backend.utils.logs import Logfire
from backend.database.schemas import UserSchema
from dataclasses import dataclass


log = Logfire(name='token-session')


@dataclass
class TokenManager:

    user_schema: UserSchema
    expire: Union[int, timedelta] = 3600
    refresh: bool = False

    def create_access_token(self) -> str:

        payload = {
            'id': str(uuid4()),
            'user': self.user_schema.model_dump(mode='json'),
            'exp': datetime.now() + timedelta(seconds=self.expire),
            'refresh': self.refresh
        }

        token = jwt.encode(payload=payload, key=Config.SUPABASE_JWT_TOKEN, algorithm=Config.ALGORITHM)
        log.fire.info('token created successfully')
        return token

    @staticmethod
    def decode_token(token: str) -> None:
        data = jwt.decode(jwt=token, key=Config.SUPABASE_JWT_TOKEN, algorithms=Config.ALGORITHM)
        log.fire.info(f'data retrieved from token: {data}')
        return data
