import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    email = Column(String(50), unique=True)
    password = Column(String(12))

    profile = relationship("Profile", back_populates="parent", uselist=False)


class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates="child")

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    name_favorite = Column(String(250), nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User")

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    terrain = Column(String(250), nullable=False)
    planet_name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(Integer)
    orbital_period = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    diameter = Column(Integer)

    favorites_id= Column(Integer, ForeignKey("favorites.id"))
    characters_id= Column(Integer, ForeignKey("characters.id"))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    hair_color = Column(String(250))
    character_name = Column(String(250), nullable=False)
    birth_year = Column(String(250))
    height = Column(Integer)
    gender = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))

    favorites_id= Column(Integer, ForeignKey("favorites.id"))
    planets_id= Column(Integer, ForeignKey("planets.id"))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')