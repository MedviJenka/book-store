import supabase
from backend.api.book import BookSchema
from backend.settings import SUPABASE_URL, SUPABASE_API_KEY
from backend.utils.logs import Logfire


log = Logfire(name='book-db')


class DatabaseManager:

    def __init__(self) -> None:
        self.db = supabase.create_client(supabase_url=SUPABASE_URL, supabase_key=SUPABASE_API_KEY)


class BooksDB(DatabaseManager):

    __table: str = 'books'

    def get_all_books(self) -> list[dict]:
        result = self.db.table(table_name=self.__table).select('*').execute()
        log.fire.info(f'found {len(result.data)} in books db')
        return result.data

    def add_book(self, schema: BookSchema) -> None:
        return self.db.table(table_name=self.__table).insert(schema.model_dump(mode='json', exclude_none=True)).execute()
