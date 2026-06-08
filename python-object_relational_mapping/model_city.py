#!/usr/bin/python3
"""Define the City class mapped to the MySQL table 'cities'."""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Represent a city stored in the 'cities' table."""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
