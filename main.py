''' fastAPI talking to supabase '''

import os

from typing import Union
from fastapi import FastAPI
from supabase import create_client, Client

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/monsters")
async def get_monsters():
    data = supabase.table("monsters").select('name').execute()
    return data.data

@app.get("/monsters/{name}")
def read_monster(name: str, q: Union[str, None] = None):
    data = supabase.table("monsters").select('*').eq("name", name).execute()
    return data.data
