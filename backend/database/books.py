from functools import cached_property
from typing import Final
from pydantic import UUID4
from backend.api.v1.books.api import BookSchema
from backend.utils.logs import Logfire
from backend.database.manager import DatabaseManager


log = Logfire(name='books-db')


class BooksDB(DatabaseManager):

    __table_name__: Final[str] = 'books'

    def get_all_books(self) -> list[dict]:
        result = self.db.table(table_name=self.__table_name__).select('*').execute()
        log.fire.info(f'found {len(result.data)} in books db')
        return result.data

    def get_book_by_id(self, book_id: UUID4):
        result = self.db.table(table_name=self.__table_name__).select('*').eq(column='id', value=book_id).execute()
        log.fire.info(f'book id: {book_id} book title: {result.data}')
        return result.data

    def get_book_by_title(self, book_title: str):
        result = self.db.table(table_name=self.__table_name__).select('title').eq(column='title', value=book_title).execute()
        log.fire.info(f'book id: {book_title} book title: {result.data}')
        return result.data

    def add_book(self, schema: BookSchema) -> None:
        result = self.db.table(table_name=self.__table_name__).insert(schema.model_dump(mode='json', exclude_none=True)).execute()
        log.fire.info(f'book added successfully: {result}')
        return result

    def update_book(self, schema: BookSchema) -> None:
        result = self.db.table(table_name=self.__table_name__).update(schema.model_dump(mode='json', exclude_none=True)).eq(column='id', value=schema.id).execute()
        log.fire.info(f'book: {schema.id} updated successfully')
        return result

    def delete_book(self, book_id: UUID4) -> None:
        result = self.db.table(table_name=self.__table_name__).delete().eq(column='id', value=book_id).execute()
        log.fire.info(f'book: {book_id} deleted successfully')
        return result
