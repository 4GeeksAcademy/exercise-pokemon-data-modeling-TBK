import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Pokemon(Base):
    __tablename__ = 'pokemon'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    PokemonID = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)

class PokemonData(Base):
    __tablename__ = 'pokemondata'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    PokemonID = Column(Integer, primary_key=True, nullable=False)
    Name = Column(String(25), nullable=False)
    Type_1 = Column(String(10), nullable=False)
    Type_2 = Column(String(10), nullable=True)
    Height = Column(Integer, primary_key=True, nullable=False)
    Weight = Column(Integer, primary_key=True, nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
