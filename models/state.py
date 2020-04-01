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
    id = BaseModel().id
    name = Column(String(128), nullable=False)
    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        cities = relationship('City', cascade="all,delete", backref="state")
    # missing something
    """
        for FileStorage: getter attribute cities that 
        returns the list of City instances with state_id
        equals to the current State.id => It will be the FileStorage 
        relationship between State and City
    """
