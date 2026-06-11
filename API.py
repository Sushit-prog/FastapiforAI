from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# this is not just schema this is a payload that we are going to get from the server
class Item(BaseModel):
  name: str
  price: int
  tax: Optional[float] = None

@app.get("/message")
async def read_root():
  return {"message": "Hello, this is Sushit"}

@app.get("/name")
async def read_root():
  return {"name": "Sushit this side"}

@app.get("/items/{item_name}")
async def get_items(item_name: str, company: str|None = None):
  # actions
  # actions for none
  data_dict ={
    "name": item_name,
    "price": 100,
    "offer": 20
  }
  # return {"item_name": item_name, "company":company}
  return Item(**data_dict)

# @app.get("/items/")
# async def all_items(skip: int = 0, limit: int = 10):
#     dummy_data = [
#         {"name": "lap1", "price":100},
#         {"name": "lap2", "price":200, "tax":10.10},
#         {"name": "lap3", "price":200}
#     ]

#     data = dummy_data[skip:skip+limit]

#     return [Item(**item) for item in data]
