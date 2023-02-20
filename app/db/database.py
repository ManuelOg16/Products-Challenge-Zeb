# from decouple import config
import databases
import sqlalchemy
from app.config import settings
# DATABASE_URL = f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@localhost:5432/products"
database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(settings.db_url)
# metadata.create_all(engine)