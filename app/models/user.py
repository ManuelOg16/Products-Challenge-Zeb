##  ORM Table Users
import sqlalchemy as sqlalchemy
from app.db.database import metadata
from app.models.enums import RoleType

user = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String(120), unique=True),
    sqlalchemy.Column("password", sqlalchemy.String(255)),
    sqlalchemy.Column("first_name", sqlalchemy.String(200)),
    sqlalchemy.Column("last_name", sqlalchemy.String(200)),
    sqlalchemy.Column("phone", sqlalchemy.String(20)),
    sqlalchemy.Column("role", sqlalchemy.Enum(RoleType),
                        nullable=False, server_default=RoleType.anonymous_user.name)
)
