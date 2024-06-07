from typing import Optional
from pydantic import BaseModel

class Client(BaseModel):
    first_name: str
    last_name: str
    email: Optional[str]
    phone: Optional[str]


class ClientUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone: Optional[str]