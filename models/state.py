#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base, Column, String, relationship,\
        getenv

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="all,delete", backref="state")
    """
        for FileStorage: getter attribute cities that
        returns the list of City instances with state_id
        equals to the current State.id => It will be the FileStorage
        relationship between State and City
    """
    @property
    def cities(self):
        from models import storage
        """
         getter attribute cities that returns the list of City instances with
         state_id equals to the current State.id => It will be the FileStorage
         relationship between State and City
        """
        cities = {}
        for key, value in storage.all(City):
            if self.id == value.state_id:
                cities[key] = value
        return cities

