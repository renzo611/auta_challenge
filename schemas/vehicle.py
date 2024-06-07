from pydantic import BaseModel

class Vehicle(BaseModel):
    brand: str
    model: str
    year: int
    price: int

