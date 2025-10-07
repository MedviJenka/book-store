import supabase
from backend.utils.logs import Logfire
from backend.settings import SUPABASE_URL, SUPABASE_API_KEY


log = Logfire(name='db-manager')


class DatabaseManager:

    def __init__(self, admin: bool = False) -> None:

        try:
            self.db = supabase.create_client(supabase_url=SUPABASE_URL, supabase_key=SUPABASE_API_KEY)

            if admin:
                self.db.postgrest.auth(token=SUPABASE_API_KEY)

            log.fire.info('db initialized successfully')

        except Exception as e:
            log.fire.error(f'db initialization error {e}')
            raise
