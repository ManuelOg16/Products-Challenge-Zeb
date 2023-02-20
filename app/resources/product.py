from fastapi import APIRouter, Depends
from starlette.requests import Request

from app.utils.send_email import send_email_async
from app.managers.auth import  oauth2_scheme, is_admin, is_super_admin
from app.managers.product import ProductManager
from app.managers.catalogue import CatalogueManager
from app.managers.user import UserManager
from app.managers.count_request import CountRequestManager
from app.schemas.request.product import ProductIn
from app.schemas.base import UpdateBaseProduct
from app.schemas.response.product import ProductOut,StandardManyOpResponse
from app.utils.generic import genera_respuesta
from app.reusable.exceptions import OPException
from app.reusable.errors import PR_500, PR_404, PR_409, PR_422 
from sqlalchemy.exc import SQLAlchemyError
import traceback
import asyncio

router = APIRouter(tags=["Products"])
counter_lock = asyncio.Lock()
counter = 0

def is_adm_or_super():
    if is_super_admin == is_super_admin:
        adm_or_sup = is_super_admin
    elif is_admin == is_admin:
        adm_or_sup= is_admin
    return adm_or_sup

async def count_product_id(user_name, product_name):
        global counter
        async with counter_lock:
            counter = 0
            counter += 1
        count_request_data = {
                "name_user": user_name,
                "name_product": product_name,
                "count":counter
                }
        await CountRequestManager.create_count_request(count_request_data)


async def  send_emails_n(product_dict, get_product):
        list_admin = []
        users = await UserManager.get_users()
        for  fields in users:
            role= fields.role
            if role == "admin": 
                email = fields.email
                list_admin.append(str(email))
        product_name=get_product.name
        listOfValues = product_dict.values()
        listOfValues = list(listOfValues)
        subject = 'Update fields in product'
        body = f" A administrator Updated the following  items: {listOfValues} of the  product {product_name}"
        email=list_admin
        if len(list_admin) > 0:
            await  send_email_async(subject,email,body)

@router.get(
    "/products/",
    response_model=StandardManyOpResponse,
    status_code=200,
)
async def get_products():
    try:
        products = await ProductManager.get_products()
        if len(products) == 0:
            raise OPException(payload=PR_404)
        response = genera_respuesta(data=products, method="GET")
    except SQLAlchemyError as e:
        raise OPException(payload=PR_500,
        data={"error": ''.join(traceback.format_exception(type(e), e, e.__traceback__)[:-1])}
            )
    return response

@router.post(
    "/products/",
    dependencies=[Depends(oauth2_scheme), Depends(is_adm_or_super())],
    response_model=ProductOut,
    status_code=201
)
async def create_product(request: Request, product: ProductIn):
    try:
        catalogue_id= int(product.catalog_id)
        get_catalogue = await CatalogueManager.get_catalogue_by_id(catalogue_id)
        if not get_catalogue:
            raise OPException(payload=PR_422)
        name = str(product.name)
        name_exists = await ProductManager.get_product_by_name(name)
        if not name_exists:
            user = request.state.user
            response = await ProductManager.create_product(product, user)
        elif  name_exists.name == name:
            raise OPException(payload=PR_409)
    except SQLAlchemyError as e:
        raise OPException(payload=PR_500,
        data={"error": ''.join(traceback.format_exception(type(e), e, e.__traceback__)[:-1])})
    return response

@router.delete(
    "/products/{product_id}/",
    dependencies=[Depends(oauth2_scheme), Depends(is_adm_or_super())],
    status_code=200,
)
async def delete_product(product_id: int):
    try:
        get_product=await ProductManager.get_product_by_id(product_id)
        if not get_product:
            raise OPException(payload=PR_404)
        else:
            products = await ProductManager.delete(product_id)
            response = genera_respuesta(data=products, method="DELETE")
    except SQLAlchemyError as e:
        raise OPException(payload=PR_500,
            data={"error": ''.join(traceback.format_exception(type(e), e, e.__traceback__)[:-1])})
    return response

@router.get(
    "/products/{product_id}/",
    dependencies=[Depends(oauth2_scheme)],
    status_code=200,
)
async def get_product_id(request: Request, product_id: int):
    try:
        get_product= await ProductManager.get_product_by_id(product_id)
        if not get_product:
            raise OPException(payload=PR_404)
        else:
            user = request.state.user
            user= await UserManager.get_user_id(user["id"])
            product = await ProductManager.get_product_by_id(product_id)
            role_user = str(user.role)
            if role_user == "anonymous_user":
                user_name=user.first_name
                product_name = product.name
                await count_product_id(user_name, product_name)
            response = genera_respuesta(data=product, method="GET")
    except SQLAlchemyError as e:
        raise OPException(payload=PR_500,
            data={"error": ''.join(traceback.format_exception(type(e), e, e.__traceback__)[:-1])})
    return response

@router.patch(
    "/products/{product_id}/",
    dependencies=[Depends(oauth2_scheme), Depends(is_adm_or_super())],
    status_code=200,
)
async def update_product(product_id: int, product: UpdateBaseProduct):
    try:
        get_product= await ProductManager.get_product_by_id(product_id)
        if not get_product:
            raise OPException(payload=PR_404)
        else:
            product_dict= product.dict(exclude_unset=True)
            if  not product_dict:
                raise OPException(payload=PR_404)
            await send_emails_n(product_dict,get_product)
            await ProductManager.update_product(product_id, product_dict)
            response = genera_respuesta(data=product, method="PATCH")
    except SQLAlchemyError as e:
        raise OPException(payload=PR_500,
                        data={"error": ''.join(traceback.format_exception(type(e), e, e.__traceback__)[:-1])})
    return response
