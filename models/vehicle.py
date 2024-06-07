from database.config import metadata, engine
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String

vehicle = Table("vehicles", metadata,
               Column("id", Integer, primary_key=True, autoincrement=True),
               Column("brand", String(50), nullable=False),
               Column("model", String(50), nullable=False),
               Column("year", Integer),
               Column("price", Integer, nullable=False),
               autoload_with=engine, extend_existing=True)