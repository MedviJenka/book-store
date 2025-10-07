from typing import Optional
from backend.utils.logs import Logfire
from backend.database.manager import DatabaseManager
from backend.settings import SUPABASE_URL, SUPABASE_API_KEY, SUPABASE_ROLE_KEY


log = Logfire(name='auth-functions')


class Auth(DatabaseManager):

    def send_magic_link(self, email: str) -> None:
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

    @staticmethod
    def get_user_data_by_email_admin(email: str) -> Optional[dict]:
        """Query the GoTrue Admin API by email (requires SERVICE_ROLE)."""
        import requests
        url = f"{SUPABASE_URL}/auth/v1/admin/users"
        headers = {"apikey": SUPABASE_API_KEY, "Authorization": f"Bearer {SUPABASE_ROLE_KEY}"}
        r = requests.get(url, headers=headers, params={"email": email}, timeout=10)
        r.raise_for_status()
        data = r.json()
        users = data["users"]
        return users[0] if users else None
