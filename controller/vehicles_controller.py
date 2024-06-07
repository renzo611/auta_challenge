from fastapi import APIRouter, Response, HTTPException
from services.vehicles_service import VehicleService
from schemas.vehicle import Vehicle
from starlette.status import HTTP_200_OK

app = APIRouter()


@app.get("/all")
async def get_all():
    return VehicleService.get_all_vehicles()

@app.get("/{vehicle_id}")
async def get_vehicle_by_id(vehicle_id: int):
    result = VehicleService.get_vehicle_by_id(vehicle_id)
    if not result:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return result

@app.post("/create")
async def create_vehicle(vehicle: Vehicle):
    return VehicleService.create_vehicle(vehicle)

@app.delete("/{id}")
async def deleteVehicle(id: int):
    VehicleService.delete_vehicle(id)
    return Response(status_code=HTTP_200_OK)

@app.put("/{id}")
async def updateVehicle(id: int, vehicle: Vehicle):
    return VehicleService.update_vehicle(id, vehicle)