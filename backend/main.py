from fastapi import FastAPI, Depends
import os
from supabase import acreate_client, AsyncClient, Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.getenv("DB_URL")
key: str = os.getenv("DB_APIKEY")

app = FastAPI()

async def create_supabase():
  supabase: AsyncClient = await acreate_client(url, key)
  return supabase

@app.get("/products")
async def getProducts(supabase: Client = Depends(create_supabase)):
    response = (
        await supabase.table("product")
        .select("*")
        .execute()
    )
    return response.data

@app.get("/products/{product_id}")
async def getProductById(product_id: int, supabase: Client = Depends(create_supabase)):
   response = (
      await supabase.table("product")
      .select("*")
      .eq("id", product_id)
      .execute()
   )
   return response.data