from typing import List

from sqlalchemy.orm import Session

from .models import Car


def get_cars(db: Session) -> List[Car]:
    return db.query(Car).all()
