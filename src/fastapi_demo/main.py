from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

title = 'FastAPI Demo'
description = 'Simple API implementation usign FastAPI framework '
version = '0.0.1'

app = FastAPI(title=title, description=description, version=version)


class Car(BaseModel):
    make: str
    model: str
    year: int


@app.get('/cars/', response_model=List[Car])
def list_cars():
    cars = [
        Car(make='Audi', model='A3', year=2005),
        Car(make='Mercedes-Benz', model='E', year=2003),
        Car(make='Tesla', model='Model S', year=2012),
    ]

    return cars
