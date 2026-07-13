# create portfolio model

from pydantic import BaseModel
from typing import List

class Holding(BaseModel):
    stock:str   # stocks
    quantity:int
    buy_price:float

class PortfolioRequest(BaseModel):
    holdings:List[Holding]