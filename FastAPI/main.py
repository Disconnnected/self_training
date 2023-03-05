from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

response = {
    "message": "hello"
}


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.get("/")
async def root():
    return response


@app.post("/items/")
async def create_item(item: Item):

    return item
