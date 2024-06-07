from fastapi import APIRouter, HTTPException
from schemas.appointment import Appointment, AppointmentUpdate
from services.appointment_service import AppointmentService

app = APIRouter()


@app.get("/all")
async def get_all_appointments():
    return AppointmentService.get_all_appointments()

@app.get("/{appointment_id}")
async def get_appointment_by_id(appointment_id: int):
    appointment = AppointmentService.get_appointment_by_id(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment


@app.post("/create")
async def create_appointment(appointment: Appointment):
    return AppointmentService.create_appointment(appointment)

@app.put("/{appointment_id}")
async def update_appointment(appointment_id: int, appointment_update: AppointmentUpdate):
    return AppointmentService.update_appointment(appointment_id, appointment_update)

@app.delete("/{appointment_id}")
async def delete_appointment(appointment_id: int):
    return AppointmentService.delete_appointment(appointment_id)