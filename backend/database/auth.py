from supabase import create_client
from backend.utils.logs import Logfire
from backend.database.manager import DatabaseManager
from backend.settings import Config


log = Logfire(name='auth-functions')


class Auth(DatabaseManager):

    def create_user(self, email: str, use_otp: bool = True) -> dict:
        supabase = create_client(supabase_url=Config.SUPABASE_URL, supabase_key=Config.SUPABASE_ROLE_KEY)

        if use_otp:
            self.db.auth.sign_in_with_otp(
                {
                    "email": email,
                    "options": {"email_redirect_to": "http://localhost:5000/welcome"},
                }
            )
            log.fire.info(f"OTP sent to {email}")
            return {"status": "otp_sent"}

        response = supabase.auth.admin.create_user({
            "email": email,
            "password": "default123",
            "email_confirm": True,
        })
        log.fire.info(f"User created: {response}")
        return response.model_dump_json()
