import os
from supabase import create_async_client, Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.getenv("DB_URL")
key: str = os.getenv("DB_APIKEY")

supabase: Client = create_async_client(url, key)