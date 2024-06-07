from database.config import con
from models.vehicle import vehicle
from schemas.vehicle import Vehicle

class VehicleService:
    @staticmethod
    def get_all_vehicles():
        result = con.execute(vehicle.select()).fetchall()
        return [{column: value for column, value in row._mapping.items()} for row in result]

    @staticmethod
    def get_vehicle_by_id(vehicle_id):
        result = con.execute(vehicle.select().where(vehicle.c.id == vehicle_id)).fetchone()
        if result:
            return {column: value for column, value in result._mapping.items()}
        return None

    @staticmethod
    def create_vehicle(vehicleRequest: Vehicle):
        result = con.execute(vehicle.insert().values(
            brand=vehicleRequest.brand,
            model=vehicleRequest.model,
            year=vehicleRequest.year,
            price=vehicleRequest.price
        ))
        return VehicleService.get_vehicle_by_id(result.lastrowid)


    @staticmethod
    def update_vehicle(vehicle_id, vehicle_request: Vehicle):
        stmt = vehicle.update().where(vehicle.c.id == vehicle_id)
        if vehicle_request.brand:
            stmt = stmt.values(brand=vehicle_request.brand)
        if vehicle_request.model:
            stmt = stmt.values(model=vehicle_request.model)
        if vehicle_request.year:
            stmt = stmt.values(year=vehicle_request.year)
        if vehicle_request.price:
            stmt = stmt.values(price=vehicle_request.price)
        con.execute(stmt)
        return {"message": "Vehicle updated successfully"}


    @staticmethod
    def delete_vehicle(vehicle_id):
        con.execute(vehicle.delete().where(vehicle.c.id == vehicle_id))
