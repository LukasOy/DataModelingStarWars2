import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class UsuarioPrincipal(Base):
    __tablename__ = 'Usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    NombreUsuario = Column(String(250), nullable=False)
    SobreNombreUsuario = Column(String(10), nullable=False)
    Mailusuario = Column(String(15), nullable=False)
    FechaSuscripcion = Column(String(15), nullable=False)

class PersonajeFavorito(Base):
    __tablename__ = 'PerFav'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Usuario_id = Column(Integer, ForeignKey('Usuario.id'))
    NombrePersonaje = Column(String(20), nullable=False)
    Personaje_id = Column(Integer, ForeignKey('Personaje.id'))

class PlanetaFavorito(Base):
    __tablename__ = 'PlaFav'
    id = Column(Integer, primary_key=True)
    Usuario_id = Column(Integer, ForeignKey('Usuario.id'))
    NombrePlaneta = Column(String(15), nullable=False)
    Planeta_id = Column(Integer, ForeignKey('Planeta.id'))

class Personajes(Base):
    __tablename__ = 'Personaje'
    id = Column(Integer, primary_key=True)
    NombrePersonaje = Column(String(20), nullable=False)
    EdadPersonaje = Column(Integer, nullable=False)
    FechaNacimiento = Column(DateTime(timezone=True), nullable=False)

class Planeta(Base):
    __tablename__='Planeta'
    id = Column(Integer, primary_key=True)
    Localizacion = Column(String(10), nullable=False)
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
