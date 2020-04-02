#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", cascade="all,delete", backref="place")
    amenities = relationship("Amenity", secondary=place_amenity,
                             backref='places', viewonly=False)
    amenity_ids = []

    @property
    def reviews(self):
        """
        the getter attribute reviews returns
        the list of Review instances
        with place_id equals to the current Place.id
        """
        from models import storage
        r = {}
        all_reviews = storage.all(Review)
        for k, v in all_reviews.items():
            if v.place_id == self.id:
                r[k] = v
        return r

    @property
    def amenities(self):
        """
        the Getter attribute amenities returns the list of Amenity instances
        based on the attribute amenity_ids
        that contains all Amenity.id linked to the Place
        """
        from models import storage
        amen = {}
        all_amen = storage.all(Amenity)
        for k, v in all_amen.items():
            if v.id in self.amenity_ids:
                amen[k] = v
        return amen

    @amenities.setter
    def amenities(self, obj):
        """ adds Amenity.id to amenity_ids"""
        if obj is not None and obj.__class__.__name__ == "Amenity":
            self.amenity_ids.append(obj.id)
