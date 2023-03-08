### Database Connection and Configuration
import os
import databases
import sqlalchemy


###GCP
# from dotenv import load_dotenv
# load_dotenv()
# user= os.getenv("DB_USER")
# password= os.getenv("DB_PASSWORD")
# host=os.getenv("DB_HOST_NAME")
# db_name=os.getenv("DB_NAME")
# port= os.getenv("DB_PORT")
# DATABASE_URL = f"postgresql+pg8000://{user}:{password}@{host}:{port}/{db_name}"
# database = databases.Database(DATABASE_URL)
# metadata = sqlalchemy.MetaData()
# engine = sqlalchemy.create_engine(DATABASE_URL)

###local
from app.config import settings
database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(settings.db_url)







