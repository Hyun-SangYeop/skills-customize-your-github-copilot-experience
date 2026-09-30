from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Inventory API")

items = []


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI API!"}


@app.get("/items")
def get_items():
    return items


@app.post("/items")
def create_item(item: Item):
    items.append(item.dict())
    return item
