import supabase_client
from fastapi import FastAPI

app = FastAPI()

@app.get("/getProduct")
async def getProducts():
    response = (
        supabase_client.table("product")
        .select("*")
        .execute()
    )
    return response