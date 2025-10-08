import requests
from typing import Optional
from backend.utils.logs import Logfire
from backend.database.manager import DatabaseManager
from backend.settings import Config


log = Logfire(name='auth-functions')


class Auth(DatabaseManager):

    url = f"{Config.SUPABASE_URL}/auth/v1/admin/users"

    def create_user(self, email: str) -> None:
        response = self.db.auth.sign_in_with_otp(
            {
                "email": email,
                "options": {
                    "email_redirect_to": "http://localhost:5000/welcome",
                },
            }
        )
        log.fire.info(f'{response.model_dump()}')
        return response.model_dump()
