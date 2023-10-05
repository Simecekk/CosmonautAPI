from pydantic import BaseModel


class AstronautInputType(BaseModel):
    name: str
    age: int


class AstronautType(BaseModel):
    id: int
    name: str
    age: int
