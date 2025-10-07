from typing import AsyncGenerator, Optional
from fastapi import APIRouter, FastAPI
from backend.database.auth import Auth
from backend.database.schemas import UserSchema
from backend.security.access import TokenManager
from backend.utils.logs import Logfire
from backend.settings import Config
from contextlib import asynccontextmanager
from backend.database.users import UsersDatabase


log = Logfire(name='users-api')

router = APIRouter(prefix=f'/api/{Config.API_VERSION}')

users = UsersDatabase()

auth = Auth()


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    log.fire.info('server started')
    yield
    log.fire.info('server stoped')


@router.get('/users')
def get_all_users() -> list[dict]:
    return users.get_all_users()


@router.get('/user')
def get_user(email: str) -> dict:
    return {
        email: users.get_user_id_by_email(email=email)
    }


@router.post('/create-user')
async def create_user(email: str) -> None:
    log.fire.info(f'user {email} create successfully')
    return auth.create_user(email)


@router.post('/login')
async def login(email: str) -> Optional[UserSchema]:
    user = await auth.get_user_data_by_email_admin(email)
    log.fire.info(f'user: {user}')
    token = TokenManager(user_schema=UserSchema(email=email, is_created=True))
    if user is not None:
        token.create_access_token()

    log.fire.info(f'user {email} was not found')
    return UserSchema(email=email, is_created=False)


@router.patch('/user')
def update_user() -> None: ...


@router.delete('/user')
def delete_user() -> None: ...
