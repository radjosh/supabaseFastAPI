''' fastAPI talking to supabase '''

'''''''''''''''''''''''''''''''''''''''''''''''''''
WARNING: NO AUTH WHATSOEVER. NOT FOR PRODUCTION

This was built entirely as a PoC for learning purposes.
Not for learning auth
Just for learning to update from react => fastapi => supabase

only deployed on a local machine etc.

NOT FOR PRODUCTION
'''''''''''''''''''''''''''''''''''''''''''''''''''

import os
from typing import Union
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware  
from pydantic import BaseModel
from supabase import create_client, Client

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class Monster(BaseModel):
    name: str
    alignment: str

app = FastAPI()

origins = [
    "http://localhost:1233",
    "http://127.0.0.1:1233",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    return response

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/monsters")
async def create_monster(monster: Monster):
    print("got there")
    data = {
        "name": monster.name,
        "alignment": monster.alignment,
    }

    response = supabase.table("monsters").insert(data).execute()

    # if response.error:
    #     print("Supabase Error:", response.error)  # Log the error for debugging
    #     raise HTTPException(status_code=400, detail=response.error)

    return response.data

@app.get("/monsters")
async def get_monsters():
    data = supabase.table("monsters").select('name').execute()
    return data.data

@app.get("/monsters/{name}")
def read_monster(name: str, q: Union[str, None] = None):
    data = supabase.table("monsters").select('*').eq("name", name).execute()
    return data.data
