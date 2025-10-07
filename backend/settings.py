import os
from dotenv import load_dotenv


load_dotenv()


API_VERSION = os.getenv('API_VERSION')

LOGFIRE_TOKEN = os.getenv('LOGFIRE_TOKEN')

SUPABASE_URL = os.getenv('SUPABASE_URL')

SUPABASE_API_KEY = os.getenv('SUPABASE_API_KEY')

SUPABASE_JWT_TOKEN = os.getenv('SUPABASE_JWT_TOKEN')

SUPABASE_ROLE_KEY = os.getenv('SUPABASE_ROLE_KEY')
