from backend.database.manager import DatabaseManager
from backend.utils.logs import Logfire


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


