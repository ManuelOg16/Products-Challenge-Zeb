import asyncclick as click

from app.db.database import database
from app.managers.user import UserManager
from app.models import RoleType


@click.command()
@click.option("-f", "--first_name", type=str, required=True)
@click.option("-l", "--last_name", type=str, required=True)
@click.option("-e", "--email", type=str, required=True)
@click.option("-p", "--phone", type=str, required=True)
@click.option("-pa", "--password", type=str, required=True)
async def create_user(first_name, last_name, email, phone, password):
    user_data = {"first_name": first_name, "last_name": last_name, "email": email, "phone": phone, "password": password, "role": RoleType.super_admin}
    await database.connect()
    await UserManager.register(user_data)
    await database.disconnect()

if __name__ == "__main__":
    create_user(_anyio_backend="asyncio") # Recomendation anyio the docs
