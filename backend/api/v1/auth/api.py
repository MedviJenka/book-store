from contextlib import asynccontextmanager
from typing import List, AsyncGenerator
from pydantic import UUID4
from fastapi import APIRouter, FastAPI
from backend.utils.logs import Logfire
from datetime import datetime, timezone
from backend.settings import API_VERSION
from backend.api.v1.books.schemas import BookSchema
from backend.database.books import BooksDB


log = Logfire(name='book-api')

router = APIRouter(prefix=f'/api/{API_VERSION}')

book = BooksDB()


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    log.fire.info('server started')
    yield
    log.fire.info('server stoped')


@router.get('/books')
async def get_all_books() -> List[dict]:
    return book.get_all_books()


@router.get('/book_id', response_model=BookSchema)
async def get_book_by_id(book_id: UUID4) -> BookSchema:
    return book.get_book_by_id(book_id=book_id)


@router.get('/book_title', response_model=BookSchema)
async def get_book_by_title(book_title: str) -> BookSchema:
    return book.get_book_by_title(book_title=book_title)


@router.post('/book')
async def add_book(schema: BookSchema) -> None:
    result = schema.model_dump(mode='json', exclude_none=True)
    return book.add_book(**result)


@router.patch('/book')
async def update_book(book_id: UUID4, title: str, author: str) -> None:
    schema = BookSchema(id=book_id, title=title, author=author, publish_date=datetime.now(timezone.utc))
    return book.update_book(schema=schema)


@router.delete('/book')
async def delete_book(book_id: UUID4) -> None:
    return book.delete_book(book_id=book_id)
