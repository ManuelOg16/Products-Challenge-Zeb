from app.db.database import database
from app.models import product

class ProductManager:
    @staticmethod
    async def get_products():
        return await database.fetch_all(product.select())
    @staticmethod
    async def create_product(product_data, user):
        data = product_data.dict()
        print(data)
        id_ = await database.execute(product.insert().values(**data))
        print(id_)
        return await database.fetch_one(product.select().where(product.c.id == id_))

    @staticmethod
    async def delete(product_id):
        await database.execute(product.delete().where(product.c.id == product_id))

    @staticmethod
    async def get_product_by_id(product_id):
        return await database.fetch_one(product.select().where(product.c.id == product_id))

    @staticmethod
    async def update_product(product_id, product_dict):
        await database.execute(product.update().where(product.c.id == product_id).values(product_dict))

    @staticmethod
    async def get_product_by_name(name):
        return await database.fetch_one(product.select().where(product.c.name == name))