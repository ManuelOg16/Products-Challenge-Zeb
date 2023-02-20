## SQL and Static Method Count Request
from app.db.database import database
from app.models import count_request

class CountRequestManager:

    @staticmethod
    async def get_count_requests():
        return await database.fetch_all(count_request.select())

    @staticmethod
    async def create_count_request(count_request_data):
        data = count_request_data
        print(data)
        id_ = await database.execute(count_request.insert().values(**data))
    
    @staticmethod
    async def get_count_by_users():
        query = "SELECT name_user, name_product, SUM (count) as total_count FROM public.count_requests GROUP BY name_user, name_product;"
        return await database.fetch_all(query)

    @staticmethod
    async def get_count_request_by_id(count_request_id):
        return await database.fetch_one(count_request.select().where(count_request.c.id == count_request_id))

    @staticmethod
    async def update_count_request(count_request_id, count_request_dict):
        await database.execute(count_request.update().where(count_request.c.id == count_request_id).values(count_request_dict))

