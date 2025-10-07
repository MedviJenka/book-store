from typing import Final
from backend.database.auth import Auth
from backend.utils.logs import Logfire
from dataclasses import dataclass


log = Logfire("database-config")


@dataclass
class UsersDatabase(Auth):

    __table_name__: Final = 'users'

    def __post_init__(self) -> None:
        super().__init__(admin=True)

    def get_user_id_by_email(self, email: str) -> str:
        result = self.get_user_data_by_email_admin(email).get('id')
        log.fire.info(f'user {email} id is: {result}')
        return result
