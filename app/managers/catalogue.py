## SQL and Static Method Catalogue
from app.db.database import database
from app.models import catalogue


class CatalogueManager:
    @staticmethod
    async def get_catalogs():
        q = catalogue.select()
        return await database.fetch_all(q)

    @staticmethod
    async def create_catalogue(catalogue_data, user):
        data = catalogue_data.dict()
        id_ = await database.execute(catalogue.insert().values(**data))
        return await database.fetch_one(catalogue.select().where(catalogue.c.id == id_))

    @staticmethod
    async def delete(catalogue_id):
        await database.execute(catalogue.delete().where(catalogue.c.id == catalogue_id))

    @staticmethod
    async def get_catalogue_by_id(catalogue_id):
        return await database.fetch_one(catalogue.select().where(catalogue.c.id == catalogue_id))

    @staticmethod
    async def update_catalogue(catalogue_id, catalogue_dict):
        await database.execute(catalogue.update().where(catalogue.c.id == catalogue_id).values(catalogue_dict))

    @staticmethod
    async def get_catalogue_by_title(title):
        return await database.fetch_one(catalogue.select().where(catalogue.c.title == title))