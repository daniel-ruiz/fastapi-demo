from pydantic import BaseModel


class Car(BaseModel):
    id: int
    make: str
    model: str
    year: int

    class Config:
        orm_mode = True


class CarInput(BaseModel):
    make: str
    model: str
    year: int
