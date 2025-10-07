from pydantic import UUID4
from typing import AsyncGenerator
from fastapi import APIRouter, FastAPI
from backend.utils.logs import Logfire
from backend.settings import Config
from contextlib import asynccontextmanager


log = Logfire(name='book-api')

router = APIRouter(prefix=f'/api/{Config.API_VERSION}')


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    log.fire.info('server started')
    yield
    log.fire.info('server stoped')
