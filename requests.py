from typing import Optional

from fastapi import FastAPI, Path, Query

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: int = Path(..., title="The ID of the item to get"),
#     q: Optional[str] = Query(None, alias="item-query"),
# ):
#     results = {"item_id": item_id}
#     if  q: 
#         results.upate({"q":q})
#     return results 

@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(..., title="The ID of the item to get"), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results 