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

    def get_all_users(self) -> list[dict]:
        headers = {"apikey": Config.SUPABASE_API_KEY, "Authorization": f"Bearer {Config.SUPABASE_ROLE_KEY}"}
        r = requests.get(self.url, headers=headers, timeout=10)
        r.raise_for_status()
        data = r.json()
        users = data["users"]
        return users

    async def get_user_data_by_email_admin(self, email: str) -> Optional[dict]:
        headers = {"apikey": Config.SUPABASE_API_KEY, "Authorization": f"Bearer {Config.SUPABASE_ROLE_KEY}"}
        r = requests.get(self.url, headers=headers, params={"email": email}, timeout=10)
        r.raise_for_status()
        data = r.json()
        users = data["users"]
        return users[0] if users else None
