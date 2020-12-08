from sqlalchemy import Column, Integer, String

from fastapi_demo.database import Base


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
