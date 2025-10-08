from contextlib import asynccontextmanager
from typing import List, AsyncGenerator
from pydantic import UUID4
from fastapi import APIRouter, FastAPI
from backend.utils.logs import Logfire
from backend.settings import Config
from backend.api.v1.books.schemas import BookSchema
from backend.database.books import BooksDB


log = Logfire(name='book-api')

router = APIRouter(prefix=f'/api/{Config.API_VERSION}')

book = BooksDB()


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    log.fire.info('server started')
    yield
    log.fire.info('server stoped')


@router.get('/books')
async def get_all_books() -> List[dict]:
# async def get_all_books(user_details: any = Depends(AccessTokenBearer)) -> List[dict]:
    return book.get_all_books()


@router.get('/book_id', response_model=BookSchema)
async def get_book_by_id(book_id: UUID4) -> BookSchema:
    return book.get_book_by_id(book_id=book_id)


@router.get('/book_title', response_model=BookSchema)
async def get_book_by_title(book_title: str) -> BookSchema:
    return book.get_book_by_title(book_title=book_title)


@router.post('/book')
async def add_book(schema: BookSchema) -> None:
    return book.add_book(schema=schema)


@router.patch('/book')
async def update_book(schema: BookSchema) -> None:
    return book.update_book(schema=schema)


@router.delete('/book')
async def delete_book(book_id: UUID4) -> None:
    return book.delete_book(book_id=book_id)
