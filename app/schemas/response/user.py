from app.models import RoleType
from app.schemas.base import UserBase


class UserOut(UserBase):
    id: int
    first_name: str
    last_name: str
    phone: str
    role: RoleType

