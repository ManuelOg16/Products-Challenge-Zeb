## View Users
from typing import List, Optional

from fastapi import APIRouter, Depends

from app.managers.auth import oauth2_scheme, is_super_admin
from app.managers.user import UserManager
from app.models import RoleType
from app.schemas.response.user import UserOut
from app.utils.generic import genera_respuesta
from app.reusable.exceptions import OPException
from app.reusable.errors import PR_500, PR_404, PR_406
from sqlalchemy.exc import SQLAlchemyError
import traceback

router = APIRouter(tags=["Users"])


@router.get(
    "/users/",
    dependencies=[Depends(oauth2_scheme), Depends(is_super_admin)],
    response_model=List[UserOut],
)
async def get_users(email: Optional[str] = None):
    if email:
        return await UserManager.get_user_by_email(email)
    return await UserManager.get_users()



@router.put(
    "/users/{user_id}/make-admin",
    dependencies=[Depends(oauth2_scheme), Depends(is_super_admin)],
    status_code=204,
)
async def make_admin(user_id: int):
    await UserManager.change_role(RoleType.admin, user_id)


@router.delete(
    "/users/{user_id}/delete-admin",
    dependencies=[Depends(oauth2_scheme), Depends(is_super_admin)],
    status_code=200,
)
async def delete_admin(user_id: int):
    try:
        get_user=await UserManager.get_user_id(user_id)
        if not get_user:
            raise OPException(payload=PR_404)
        elif get_user.role == "super_admin":
            raise OPException(payload=PR_406)
        else:
            user = await UserManager.delete(user_id)
            response = genera_respuesta(data=user, method="DELETE")
    except SQLAlchemyError as e:
            raise OPException(payload=PR_500,
                data={"error": ''.join(traceback.format_exception(type(e), e, e.__traceback__)[:-1])})
    return response
