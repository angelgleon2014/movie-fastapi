from bd.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

class Movie(Base):
    __tablename__ = 'movies'  # Nombre de la tabla en la base de datos

    id = Column(Integer, primary_key=True, index=True)  # ID de la película, clave primaria
    title = Column(String(100), nullable=False)  # Título de la película, no puede ser nulo
    overview = Column(String(500), nullable=True)  # Descripción de la película, puede ser nulo
    year = Column(Integer, nullable=False)  # Año de lanzamiento de la película, no puede ser nulo
    rating = Column(Integer, nullable=False)  # Calificación de la película, no puede ser nulo
    category = Column(String(50), nullable=False)  # Categoría de la película, no puede ser nulo
    created_at = Column(DateTime, nullable=False)  # Fecha y hora de creación del registro, no puede ser nulo
    updated_at = Column(DateTime, nullable=True)  # Fecha y hora de actualización del registro, puede ser nulo
    is_active = Column(Boolean, default=True)  # Indica si la película está activa o no, por defecto es True