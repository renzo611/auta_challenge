from fastapi import FastAPI
from controller import clients_controller, vehicles_controller, appointments_controller, additional_controller

app = FastAPI()

app.include_router(clients_controller.app, prefix="/clients", tags=["Clients"])
app.include_router(vehicles_controller.app, prefix="/vehicles", tags=["Vehicles"])
app.include_router(appointments_controller.app, prefix="/appointments", tags=["Appointments"])
app.include_router(additional_controller.app, prefix="/additional", tags=["First exercise"])