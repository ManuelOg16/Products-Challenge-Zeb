from datetime import datetime


from app.schemas.base import BaseProduct
from pydantic import BaseModel
from typing import Optional, List

class ProductOut(BaseProduct):
    id: int
    created_at: datetime

class StandardOneOpResponse(BaseModel):
    appCode: str
    ztCode: int
    message: str
    data: ProductOut

class StandardManyOpResponse(BaseModel):
    appCode: str
    ztCode: int
    message: str
    page: Optional[int]
    limit: Optional[int]
    total_rows: Optional[int]
    data: List[ProductOut]

