from typing import List

from sqlalchemy.orm import Session

from .models import Car
from .schemas import CarInput


def get_cars(db: Session) -> List[Car]:
    return db.query(Car).all()


def create_car(db: Session, car_input: CarInput) -> Car:
    new_car = Car(**dict(car_input))

    db.add(new_car)
    db.commit()

    return new_car
