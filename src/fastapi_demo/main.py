from typing import List

from fastapi import Depends, FastAPI, status
from sqlalchemy.orm import Session

from .database import SessionLocal
from .cars import repository, schemas

title = 'FastAPI Demo'
description = 'Simple API implementation usign FastAPI framework '
version = '0.0.1'

app = FastAPI(title=title, description=description, version=version)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get('/cars/', response_model=List[schemas.Car])
def list_cars(db: Session = Depends(get_db)):
    cars = repository.get_cars(db)

    return cars


@app.post('/cars/', response_model=schemas.Car, status_code=status.HTTP_201_CREATED)
def create_new_car(car_input: schemas.CarInput, db: Session = Depends(get_db)):
    new_car = repository.create_car(db, car_input)

    return new_car
