import supabase
from backend.settings import SUPABASE_URL, SUPABASE_API_KEY
from backend.utils.logs import Logfire


log = Logfire(name='db-manager')


class DatabaseManager:

    def __init__(self) -> None:
        try:
            self.db = supabase.create_client(supabase_url=SUPABASE_URL, supabase_key=SUPABASE_API_KEY)
            log.fire.info('db initialized successfully')
        except Exception as e:
            log.fire.error(f'db initialization error {e}')
            raise
