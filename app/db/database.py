### Database Connection and Configuration
import databases
import sqlalchemy
from app.config import settings
database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(settings.db_url)
