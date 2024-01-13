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
    pokemon_id = Column(Integer, primary_key=True,)
    name = Column(String(25), nullable=False)
    pokemontype = relationship("Pokemon_type")
    pokemonstat = relationship("Pokemon_stat")
    pokemonability = relationship("Pokemon_ability")

class Pokemon_type(Base):
    __tablename__ = 'pokemontype'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    pokemon_id = Column(Integer, ForeignKey("pokemon.pokemon_id"), nullable=False)
    pokemon_type_id = Column(Integer, primary_key=True, nullable=False)
    type_1 = Column(String(10), nullable=False)
    type_2 = Column(String(10), nullable=True)
    

class Pokemon_stat(Base):
    __tablename__ = 'pokemonstat'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    pokemon_id = Column(Integer, ForeignKey("pokemon.pokemon_id"), nullable=False)
    pokemon_stat_id = Column(Integer, primary_key=True, nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    hp = Column(Integer, nullable=False)
    attack = Column(Integer, nullable=False)
    defense = Column(Integer, nullable=False)

class Pokemon_ability(Base):
    __tablename__ = 'pokemonability'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.\
    pokemon_id = Column(Integer, ForeignKey("pokemon.pokemon_id"), nullable=False)
    pokemon_ability_id = Column(Integer, primary_key=True, nullable=False)
    ability_1 = Column(String(25), nullable=False)
    ability_2 = Column(String(25), nullable=False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
