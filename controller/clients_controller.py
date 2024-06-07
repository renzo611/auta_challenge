from fastapi import APIRouter, Response, HTTPException
from services.client_service import ClientService
from schemas.client import Client, ClientUpdate
from starlette.status import HTTP_200_OK

app = APIRouter()


@app.get("/all")
async def get_all():
    return ClientService.get_all_clients()

@app.get("/{client_id}")
async def get_client_by_id(client_id: int):
    result = ClientService.get_client_by_id(client_id)
    if not result:
        raise HTTPException(status_code=404, detail="Client not found")
    return result

@app.post("/create")
async def create_client(client: Client):
    return ClientService.create_client(client)

@app.delete("/{id}")
async def delete_client(id: int):
    ClientService.delete_client(id)
    return Response(status_code=HTTP_200_OK)

@app.put("/{id}")
async def update_client(id: int, client: ClientUpdate):
    return ClientService.update_client(id, client)