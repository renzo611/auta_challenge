from database.config import metadata, engine
from sqlalchemy import Table, Column, Enum, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, DateTime
import enum

class AppointmentType(enum.Enum):
    PURCHASE = 'PURCHASE'
    SALE = 'SALE'

appointment = Table("appointments", metadata,
                    Column("id", Integer, primary_key=True, autoincrement=True),
                    Column("appointment_date", DateTime, nullable=False),
                    Column("client_id", Integer, ForeignKey('clients.client_id')),
                    Column("vehicle_id", Integer, ForeignKey('vehicles.vehicle_id')),
                    Column("type", Enum(AppointmentType), nullable=False),
                    autoload_with=engine, extend_existing=True)