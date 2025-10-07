import jwt
from uuid import uuid4
from datetime import timedelta, datetime
from backend.settings import Config
from backend.utils.logs import Logfire
from backend.database.schemas import UserSchema


log = Logfire(name='token-session')


def create_access_token(user_data: UserSchema, expire: int = 3600, refresh: bool = False) -> None:

    payload = {
        'id': str(uuid4()),
        'user': user_data,
        'exp': datetime.now() + timedelta(seconds=expire),
        'refresh': refresh
    }

    token = jwt.encode(payload=payload, key=Config.SUPABASE_JWT_TOKEN, algorithm=Config.ALGORITHM)
    log.fire.info('token created successfully')
    return token


def decode_token(token: str) -> None:
    data = jwt.decode(kwt=token, key=Config.SUPABASE_JWT_TOKEN, algorithm=[Config.ALGORITHM])
    return data
