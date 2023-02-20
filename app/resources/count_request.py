## View Count Request
from fastapi import APIRouter, Depends
from starlette.requests import Request

from app.managers.auth import  oauth2_scheme, is_admin, is_super_admin
from app.managers.count_request import CountRequestManager
from app.utils.generic import genera_respuesta
from app.reusable.exceptions import OPException
from app.reusable.errors import PR_500, PR_404
from sqlalchemy.exc import SQLAlchemyError
import traceback

router = APIRouter(tags=["Count-Products"])

## Validation Super Admin or Admins
def is_adm_or_super():
    if is_super_admin == is_super_admin:
        adm_or_sup = is_super_admin
    elif is_admin == is_admin:
        adm_or_sup= is_admin
    return adm_or_sup

@router.get(
    "/count-by-product/",
    dependencies=[Depends(oauth2_scheme), Depends(is_adm_or_super())],
    status_code=200,
)
async def get_count_by_users(request: Request):
    try:
        count_by_users = await CountRequestManager.get_count_by_users()
        if len(count_by_users) == 0:
            raise OPException(payload=PR_404)
        response = genera_respuesta(data=count_by_users, method="GET")
    except SQLAlchemyError as e:
        raise OPException(payload=PR_500,
        data={"error": ''.join(traceback.format_exception(type(e), e, e.__traceback__)[:-1])}
            )
    return response


