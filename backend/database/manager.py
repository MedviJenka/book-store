import supabase
from backend.utils.logs import Logfire
from backend.settings import Config


log = Logfire(name='db-manager')


class DatabaseManager:

    def __init__(self, admin: bool = False) -> None:

        try:
            self.db = supabase.create_client(supabase_url=Config.SUPABASE_URL, supabase_key=Config.SUPABASE_API_KEY)

            if admin:
                self.db.postgrest.auth(token=Config.SUPABASE_API_KEY)

            log.fire.info('db initialized successfully')

        except Exception as e:
            log.fire.error(f'db initialization error {e}')
            raise
