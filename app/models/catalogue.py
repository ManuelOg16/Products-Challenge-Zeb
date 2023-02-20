##  ORM Table Catalogue
import sqlalchemy as sqlalchemy
from app.db.database import metadata, engine

catalogue = sqlalchemy.Table(
    "catalogs",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(120), nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String(250), nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
)

metadata.create_all(engine)