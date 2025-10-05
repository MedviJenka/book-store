from uuid import uuid4
from fastapi import APIRouter
from backend.settings import API_VERSION
from pydantic import BaseModel, Field, UUID4


router = APIRouter(prefix=f'/api/{API_VERSION}')


class BookSchema(BaseModel):
    id: UUID4 = Field(default=uuid4())
    title: str
    author: str


@router.post('/add_book')
async def add_book(schema: BookSchema) -> dict:
    return schema.model_dump(mode='json')

