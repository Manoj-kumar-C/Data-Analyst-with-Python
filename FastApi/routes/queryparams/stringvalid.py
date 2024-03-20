from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    q: str
    min_length: int = Query(..., gt=3)

@app.get("/items/")
async def read_items(item: Item):
    return {"q": item.q, "min_length": item.min_length}
