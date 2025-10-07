from pydantic import UUID4
from typing import AsyncGenerator
from fastapi import APIRouter, FastAPI
from backend.utils.logs import Logfire
from backend.settings import API_VERSION
from backend.database.books import BooksDB
from contextlib import asynccontextmanager


log = Logfire(name='book-api')

router = APIRouter(prefix=f'/api/{API_VERSION}')

book = BooksDB()


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    log.fire.info('server started')
    yield
    log.fire.info('server stoped')


@router.delete('/book')
async def delete_book(book_id: UUID4) -> None:
    return book.delete_book(book_id=book_id)
