##  ORM Table Product
import sqlalchemy as sqlalchemy
from app.db.database import metadata

product = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(120), nullable=False),
    sqlalchemy.Column("sku", sqlalchemy.String(200), nullable=False),
    sqlalchemy.Column("price", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("brand", sqlalchemy.String(200), nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("catalog_id", sqlalchemy.ForeignKey("catalogs.id"), nullable=False)
)

