from datetime import timedelta
from typing import AsyncGenerator
from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse
from backend.database.auth import Auth
from backend.database.schemas import UserSchema
from backend.security.access import TokenManager
from backend.utils.logs import Logfire
from backend.settings import Config
from contextlib import asynccontextmanager
from backend.database.users import UsersDatabase


log = Logfire(name='auth-api')

router = APIRouter(prefix=f'/api/{Config.API_VERSION}/auth')

users = UsersDatabase()

auth = Auth()


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    log.fire.info('auth server started')
    yield
    log.fire.info('auth server stoped')


@router.post('/create-user')
async def create_user(email: str) -> None:
    log.fire.info(f'user {email} create successfully')
    return auth.create_user(email)


@router.post('/login')
async def login(email: str) -> UserSchema or JSONResponse:

    user = auth.get_user_data_by_email_admin(email)
    log.fire.info(f'user: {user}')
    access_schema = UserSchema(email=email)
    refresh_schema = UserSchema(email=email, is_created=True)

    if user is not None:
        access_token = TokenManager(user_schema=access_schema.model_dump())
        refresh_token = TokenManager(user_schema=refresh_schema, refresh=True, expire=timedelta(days=2))
        return access_token

        # access_token.create_access_token()
        # return JSONResponse(
        #     content={
        #         'message': 'login successful',
        #         'email': email,
        #         'access_token': access_token,
        #         'refresh_token': refresh_token,
        #     }
        # )

    else:
        log.fire.info(f'user {email} was not found')
        raise
