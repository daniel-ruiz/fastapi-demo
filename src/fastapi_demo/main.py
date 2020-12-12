from typing import List

from fastapi import Depends, FastAPI
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
