import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

from core.settings import db_engine

metadata = sqlalchemy.MetaData()
Base = declarative_base(metadata=metadata)


Astronaut = sqlalchemy.Table(
    "astronauts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("age", sqlalchemy.Integer),
)


metadata.create_all(db_engine)
