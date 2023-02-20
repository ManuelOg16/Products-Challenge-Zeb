from datetime import datetime


from app.schemas.base import BaseCatalogue
from pydantic import BaseModel
from typing import Optional, List

class CatalogueOut(BaseCatalogue):
    id: int
    created_at: datetime


class StandardOneOpResponse(BaseModel):
    appCode: str
    ztCode: int
    message: str
    data: CatalogueOut

class StandardManyOpResponse(BaseModel):
    appCode: str
    ztCode: int
    message: str
    page: Optional[int]
    limit: Optional[int]
    total_rows: Optional[int]
    data: List[CatalogueOut]