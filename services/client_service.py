from database.config import con
from models.client import client
from schemas.client import ClientUpdate, Client

class ClientService:
    @staticmethod
    def get_all_clients():
        result = con.execute(client.select()).fetchall()
        return [{column: value for column, value in row._mapping.items()} for row in result]

    @staticmethod
    def get_client_by_id(client_id):
        result = con.execute(client.select().where(client.c.id == client_id)).fetchone()
        if result:
            return {column: value for column, value in result._mapping.items()}
        return None


    @staticmethod
    def create_client(client_request: Client):
        result = con.execute(client.insert().values(
                first_name=client_request.first_name,
                last_name=client_request.last_name,
                email=client_request.email,
                phone=client_request.phone
            ))
        return ClientService.get_client_by_id(result.lastrowid)

    @staticmethod
    def update_client(client_id, client_update: ClientUpdate):
        stmt = client.update().where(client.c.id == client_id)
        if client_update.first_name:
            stmt = stmt.values(first_name=client_update.first_name)
        if client_update.last_name:
            stmt = stmt.values(last_name=client_update.last_name)
        if client_update.email:
            stmt = stmt.values(email=client_update.email)
        if client_update.phone:
            stmt = stmt.values(phone=client_update.phone)
        con.execute(stmt)
        return {"message": "Client updated successfully"}


    @staticmethod
    def delete_client(client_id):
        stmt = client.delete().where(client.c.id == client_id)
        con.execute(stmt)
        return {"message": "Client deleted successfully"}