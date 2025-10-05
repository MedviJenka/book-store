from datetime import datetime, timezone
from typing import List
from fastapi import APIRouter
from pydantic import UUID4

from backend.api.schemas import BookSchema
from backend.database.manager import BooksDB
from backend.settings import API_VERSION
from backend.utils.logs import Logfire


log = Logfire(name='book-api')

router = APIRouter(prefix=f'/api/{API_VERSION}')

book = BooksDB()


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
async def add_book(title: str, author: str) -> None:
    schema = BookSchema(title=title, author=author, publish_date=datetime.now(timezone.utc))
    return book.add_book(schema=schema)


@router.patch('/book')
async def update_book(schema: BookSchema) -> dict:
    return schema.model_dump(mode='json')


@router.delete('/book')
async def delete_book(schema: BookSchema) -> None:
    del schema.id


# @router.get('/headers')
# async def get_headers(accept:       str = Header(default=None),
#                       content_type: str = Header(default='application/json'),
#                       user_agent:   str = Header(default=None),
#                       host:         str = Header(default=None)
#                       ) -> dict:
#     request_headers = {
#         'Accept': accept,
#         'Content-Type': content_type,
#         'User': user_agent,
#         'Host': host
#     }
#     return request_headers
