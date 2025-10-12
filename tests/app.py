import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter, Depends
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field, EmailStr
from typing import AsyncGenerator
from backend.utils.logs import Logfire
from uuid import uuid4, UUID
from backend.settings import Config

log = Logfire(name='app-server')


class CreateUserSchema(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    age: int
    email: EmailStr


class CreateUser:

    schema: CreateUserSchema

    def create_user(self) -> str:
        return self.schema.model_dump(mode='json')


router = APIRouter(prefix=f'/api/{Config.API_VERSION}')


@router.post('/create-user')
async def create_user(user: CreateUser = Depends(CreateUserSchema)) -> str:
    return f'{user.schema.name} created successfully'


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    log.fire.info('server started')
    yield
    log.fire.info('server shutdown')

app = FastAPI()

app.include_router(router)


@app.get('/')
async def root() -> RedirectResponse:
    return RedirectResponse('docs')


@app.get('health')
async def health() -> dict:
    return {'status': 200, 'health': 'healthy'}


if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=9876, use_colors=True)
