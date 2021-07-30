from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/collection/{resource_id}")
async def read_resource(resource_id):
    return {"resource_id": resource_id}

@app.post("/items/")
async def create_item(item: Item):
    return item