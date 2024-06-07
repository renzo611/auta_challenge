from database.config import metadata, engine
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String

client = Table("clients", metadata,
               Column("id", Integer, primary_key=True, autoincrement=True),
               Column("first_name", String(100), nullable=False),
               Column("last_name", String(100), nullable=False),
               Column("email", String(100)),
               Column("phone", String(20)),
               autoload_with=engine, extend_existing=True)