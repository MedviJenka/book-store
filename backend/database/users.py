from backend.database.auth import Auth
from backend.database.manager import DatabaseManager
from backend.settings import SUPABASE_JWT_TOKEN
from backend.utils.logs import Logfire


log = Logfire(name='users-db')


class UsersDatabase(Auth):

    def create_user(self, email: str) -> None:
        log.fire.info(f'user email: {email} created')
        return self.send_magic_link(email=email)

    def get_user_by_email(self) -> None:
        return self.db.auth.get_user(SUPABASE_JWT_TOKEN)


print(UsersDatabase().get_user_by_email())
