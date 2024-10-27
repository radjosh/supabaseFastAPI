''' just supabase, no fastAPI '''

import os

from supabase import create_client, Client

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]
USERNAME = os.environ["SUPABASE_USERNAME"]
PASSWORD = os.environ["SUPABASE_PASSWORD"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

response = supabase.auth.sign_up({"email": "radjosh@gmail.com", "password": "@EFEFefef2"})