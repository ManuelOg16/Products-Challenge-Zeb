from fastapi import APIRouter, Depends
from starlette.requests import Request

from app.managers.auth import  oauth2_scheme, is_admin, is_super_admin
from app.managers.catalogue import CatalogueManager
from app.schemas.request.catalogue import CatalogueIn
from app.schemas.base import UpdateBaseCatalogue
from app.schemas.response.catalogue import CatalogueOut, StandardManyOpResponse
from app.utils.generic import genera_respuesta
from app.reusable.exceptions import OPException
from app.reusable.errors import PR_500, PR_404, PR_409
from sqlalchemy.exc import SQLAlchemyError
import traceback

router = APIRouter(tags=["Catalogs"])

def is_adm_or_super():
    if is_super_admin == is_super_admin:
        adm_or_sup = is_super_admin
    elif is_admin == is_admin:
        adm_or_sup= is_admin
    return adm_or_sup

@router.get(
    "/catalogs/",
    response_model=StandardManyOpResponse,
    status_code=200,
)
async def get_catalogs(request: Request):
    try:
        catalogs = await CatalogueManager.get_catalogs()
        if len(catalogs) == 0:
            raise OPException(payload=PR_404)
        response = genera_respuesta(data=catalogs, method="GET")
    except SQLAlchemyError as e:
        raise OPException(payload=PR_500,
        data={"error": ''.join(traceback.format_exception(type(e), e, e.__traceback__)[:-1])}
            )
    return response

@router.post(
    "/catalogs/",
    dependencies=[Depends(oauth2_scheme), Depends(is_adm_or_super())],
    response_model=CatalogueOut,
    status_code=201
)
async def create_catalogue(request: Request, catalogue: CatalogueIn):
    try:
        title = str(catalogue.title)
        title_exists = await CatalogueManager.get_catalogue_by_title(title)
        user = request.state.user
        if not title_exists:
            user = request.state.user
            response = await CatalogueManager.create_catalogue(catalogue, user)
        elif  title_exists.title == title:
            raise OPException(payload=PR_409)
    except SQLAlchemyError as e:
        raise OPException(payload=PR_500,
        data={"error": ''.join(traceback.format_exception(type(e), e, e.__traceback__)[:-1])})
    return response

@router.delete(
    "/catalogs/{catalogue_id}/",
    dependencies=[Depends(oauth2_scheme), Depends(is_adm_or_super())],
    status_code=200,
)
async def delete_catalogue(catalogue_id: int):
    try:
        get_catalogue = await CatalogueManager.get_catalogue_by_id(catalogue_id)
        if not get_catalogue:
            raise OPException(payload=PR_404)
        else:
            catalogs = await CatalogueManager.delete(catalogue_id)
            response = genera_respuesta(data=catalogs, method="DELETE")
    except SQLAlchemyError as e:
        raise OPException(payload=PR_500,
            data={"error": ''.join(traceback.format_exception(type(e), e, e.__traceback__)[:-1])})
    return response

@router.get(
    "/catalogs/{catalogue_id}/",
    dependencies=[Depends(oauth2_scheme)],
    status_code=200,
)
async def get_catalogue_id(catalogue_id: int):
    try:
        get_catalogue = await CatalogueManager.get_catalogue_by_id(catalogue_id)
        if not get_catalogue:
            raise OPException(payload=PR_404)
        else:
            catalogue = await CatalogueManager.get_catalogue_by_id(catalogue_id)
            response = genera_respuesta(data=catalogue, method="GET")
    except SQLAlchemyError as e:
        raise OPException(payload=PR_500,
            data={"error": ''.join(traceback.format_exception(type(e), e, e.__traceback__)[:-1])})
    return response

@router.patch(
    "/catalogs/{catalogue_id}/",
    dependencies=[Depends(oauth2_scheme), Depends(is_adm_or_super())],
    status_code=200,
)
async def update_catalogue(catalogue_id: int, catalogue: UpdateBaseCatalogue):
    try:
        get_catalogue = await CatalogueManager.get_catalogue_by_id(catalogue_id)
        if not get_catalogue:
            raise OPException(payload=PR_404)
        else:
            catalogue_dict = catalogue.dict(exclude_unset=True)
            catalogue = await CatalogueManager.update_catalogue(catalogue_id, catalogue_dict)
            response = genera_respuesta(data=catalogue, method="PATCH")
    except SQLAlchemyError as e:
        raise OPException(payload=PR_500,
                        data={"error": ''.join(traceback.format_exception(type(e), e, e.__traceback__)[:-1])})
    return response
