from sqlalchemy import update, select
from database.config import engine, con
from models import appointment as p, client, vehicle
from schemas.appointment import Appointment, AppointmentUpdate

class AppointmentService:

    @staticmethod
    def get_all_appointments():
        with engine.connect() as conn:
            stmt = select(
                p.c.id.label('appointment_id'),
                p.c.appointment_date,
                p.c.type,
                client.c.id.label('client_id'),
                client.c.first_name,
                client.c.last_name,
                vehicle.c.id.label('vehicle_id'),
                vehicle.c.brand,
                vehicle.c.model
            ).select_from(
                p.join(client, p.c.client_id == client.c.id).join(vehicle, p.c.vehicle_id == vehicle.c.id)
            )

            result = conn.execute(stmt).fetchall()
            appointments = []
            for row in result:
                appointment = {
                    "appointment_id": row.appointment_id,
                    "appointment_date": row.appointment_date,
                    "type": row.type,
                    "client": {
                        "client_id": row.client_id,
                        "first_name": row.first_name,
                        "last_name": row.last_name
                    },
                    "vehicle": {
                        "vehicle_id": row.vehicle_id,
                        "brand": row.brand,
                        "model": row.model
                    }
                }
                appointments.append(appointment)

            return appointments

    @staticmethod
    def get_appointment_by_id(appointment_id: int):
        with engine.connect() as conn:
            stmt = select(
                p.c.id.label('appointment_id'),
                p.c.appointment_date,
                p.c.type,
                client.c.id.label('client_id'),
                client.c.first_name,
                client.c.last_name,
                vehicle.c.id.label('vehicle_id'),
                vehicle.c.brand,
                vehicle.c.model
            ).select_from(
                p.join(client, p.c.client_id == client.c.id).join(vehicle, p.c.vehicle_id == vehicle.c.id)
            ).where(p.c.id == appointment_id)

            result = conn.execute(stmt).fetchone()
            if result:
                return {
                    "appointment_id": result.appointment_id,
                    "appointment_date": result.appointment_date,
                    "type": result.type,
                    "client": {
                        "client_id": result.client_id,
                        "first_name": result.first_name,
                        "last_name": result.last_name
                    },
                    "vehicle": {
                        "vehicle_id": result.vehicle_id,
                        "brand": result.brand,
                        "model": result.model
                    }
                }
            return None

    @staticmethod
    def create_appointment(appointment_create: Appointment):
        client_result = con.execute(client.select().where(p.c.id == appointment_create.client_id)).fetchone()
        vehicle_result = con.execute(vehicle.select().where(p.c.id == appointment_create.vehicle_id)).fetchone()

        if client_result is None:
            return {"error": "Client doesn't exist", "status_code": 404}
        elif vehicle_result is None:
            return {"error": "Vehicle doesn't exist", "status_code": 404}


        result = con.execute(p.insert().values(
                appointment_date=appointment_create.appointment_date,
                client_id=appointment_create.client_id,
                vehicle_id=appointment_create.vehicle_id,
                type=appointment_create.type
            ))
        return {"data": AppointmentService.get_appointment_by_id(result.lastrowid), "status_code": 201}


    @staticmethod
    def update_appointment(appointment_id, appointment_update: AppointmentUpdate):
        with engine.connect() as conn:
            stmt = update(p).where(p.c.id == appointment_id)
            if appointment_update.appointment_date:
                stmt = stmt.values(appointment_date=appointment_update.appointment_date)
            if appointment_update.client_id:
                client_result = con.execute(
                    client.select().where(p.c.id == appointment_update.client_id)).fetchone()
                if client_result is None:
                    return {"error": "Client doesn't exist", "status_code": 404}
                stmt = stmt.values(client_id=appointment_update.client_id)
            if appointment_update.vehicle_id:
                vehicle_result = con.execute(
                    vehicle.select().where(p.c.id == appointment_update.vehicle_id)).fetchone()
                if vehicle_result is None:
                    return {"error": "Vehicle doesn't exist", "status_code": 404}
                stmt = stmt.values(vehicle_id=appointment_update.vehicle_id)
            if appointment_update.type:
                stmt = stmt.values(type=appointment_update.type)
            conn.execute(stmt)
            return {"message": "Appointment updated successfully"}

    @staticmethod
    def delete_appointment(appointment_id: int):
        stmt = p.delete().where(p.c.id == appointment_id)
        con.execute(stmt)
        return {"message": "Appointment deleted successfully"}
