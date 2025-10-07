from typing import AsyncGenerator
from fastapi import APIRouter, FastAPI
from backend.utils.logs import Logfire
from backend.settings import API_VERSION
from contextlib import asynccontextmanager
from backend.database.users import UsersDatabase


log = Logfire(name='book-api')

router = APIRouter(prefix=f'/api/{API_VERSION}')

users = UsersDatabase()


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    log.fire.info('server started')
    yield
    log.fire.info('server stoped')


@router.get('/users')
def get_all_users() -> None: ...


@router.get('/user')
def get_user() -> None: ...


@router.post('/user')
def add_user() -> None: ...


@router.patch('/user')
def update_user() -> None: ...


@router.delete('/user')
def delete_user() -> None: ...
