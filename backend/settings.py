import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


load_dotenv()


class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    API_VERSION: str = os.getenv('API_VERSION')

    LOGFIRE_TOKEN: str = os.getenv('LOGFIRE_TOKEN')

    SUPABASE_URL: str = os.getenv('SUPABASE_URL')

    SUPABASE_API_KEY: str = os.getenv('SUPABASE_API_KEY')

    SUPABASE_JWT_TOKEN: str = os.getenv('SUPABASE_JWT_TOKEN')

    SUPABASE_ROLE_KEY: str = os.getenv('SUPABASE_ROLE_KEY')

    ALGORITHM: str = 'HS256'


Config = Settings()
