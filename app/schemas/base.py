from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    
class BaseProduct(BaseModel):
    name: str
    sku: str
    price: float
    brand: str
    catalog_id: int
    
class UpdateBaseProduct(BaseModel):
    name: str = None
    sku: str = None
    price: float = None
    brand: str = None
    catalog_id: int = None

class BaseCatalogue(BaseModel):
    title: str
    description: str
    
class UpdateBaseCatalogue(BaseModel):
    title: str = None
    description: str = None


