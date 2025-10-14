import requests
from typing import Final, Optional
from backend.database.auth import Auth
from backend.settings import Config
from backend.utils.logs import Logfire
from dataclasses import dataclass


log = Logfire("database-config")


@dataclass
class UsersDatabase(Auth):

    __table_name__: Final = 'users'

    def __post_init__(self) -> None:
        super().__init__(admin=True)

    def get_all_users(self) -> list[dict]:
        headers = {"apikey": Config.SUPABASE_API_KEY, "Authorization": f"Bearer {Config.SUPABASE_ROLE_KEY}"}
        r = requests.get(self.url, headers=headers, timeout=10)
        r.raise_for_status()
        data = r.json()
        users = data["users"]
        return users

    def get_user_data_by_email_admin(self, email: str) -> Optional[dict]:
        headers = {"apikey": Config.SUPABASE_API_KEY, "Authorization": f"Bearer {Config.SUPABASE_ROLE_KEY}"}
        r = requests.get(self.url, headers=headers, params={"email": email}, timeout=10)
        r.raise_for_status()
        data = r.json()
        log.fire.info(f'{data}')
        return data

    def get_user_id_by_email(self, email: str) -> str:
        result = self.get_user_data_by_email_admin(email).get('id')
        log.fire.info(f'user {email} id is: {result}')
        return result
