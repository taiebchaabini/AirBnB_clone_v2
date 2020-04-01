#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base, Column, ForeignKey, String

class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = 'cities'
    id = BaseModel().id
    name = Column(String(128), nullable=False)
    state_id = Column(String(128), ForeignKey('states.id'), nullable=False)
