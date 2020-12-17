#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")
# all, delete, delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """
            returns the list of City instances with state_id equals
            to the current State.id
            """
            list_city = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
