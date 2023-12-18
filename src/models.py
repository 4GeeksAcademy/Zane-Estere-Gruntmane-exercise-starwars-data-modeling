import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User (Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name= Column (String (250), nullable=False)
    last_name = Column (String (250), nullable=False)

class Favorits(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    fav_planets = Column(Integer, ForeignKey('planets.id'))
    fav_people = Column(Integer, ForeignKey('people.id'))
    fav_starships = Column(Integer, ForeignKey('starships.id'))

class People(Base): 
    __tablename__ = 'People'
    id = Column(Integer, primary_key=True)
    name = Column(String())
    user_id = Column(Integer, ForeignKey('user.id'))


class Starships (Base): 
    __tablename__ = 'Starships'
    id = Column(Integer, primary_key=True)
    name = Column (String()) 
    model = Column (String())
    birth_year = Column (Integer)
    

class Planets(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
