from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from models.appointment import AppointmentType

class Appointment(BaseModel):
    appointment_date: datetime
    client_id: int
    vehicle_id: int
    type: AppointmentType


class AppointmentUpdate(BaseModel):
    appointment_date: Optional[str]
    client_id: Optional[int]
    vehicle_id: Optional[int]
    type: Optional[AppointmentType]