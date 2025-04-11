from pydantic import BaseModel
from typing import List

class OrderItemIn(BaseModel):
    product_id: int
    quantity: int

class OrderIn(BaseModel):
    items: List[OrderItemIn]

class ProductOut(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

    class Config:
        orm_mode = True
