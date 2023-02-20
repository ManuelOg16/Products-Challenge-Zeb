from fastapi import APIRouter
from app.resources import auth, product, user, catalogue, count_request


api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(catalogue.router)
api_router.include_router(product.router)
api_router.include_router(count_request.router)
api_router.include_router(user.router)
