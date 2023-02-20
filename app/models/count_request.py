##  ORM Table Count Request
import sqlalchemy as sqlalchemy
from app.db.database import metadata, engine

count_request = sqlalchemy.Table(
    "count_requests",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name_user", sqlalchemy.String(120), nullable=False),
    sqlalchemy.Column("name_product", sqlalchemy.String(120), nullable=False),
    sqlalchemy.Column("count", sqlalchemy.BigInteger, nullable=False),
)

metadata.create_all(engine)