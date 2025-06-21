import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqliteName = "movies.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))# Obtiene el directorio actual del archivo
# sqlite_path = os.path.join(base_dir, sqliteName)  # Construye la ruta completa al archivo SQLite
databaseUrl = f"sqlite:///{os.path.join(base_dir, sqliteName)}"  # Crea la URL de conexión a la base de datos SQLite

# engine = create_engine(databaseUrl, connect_args={"check_same_thread": False})  # Crea el motor de la base de datos SQLite

engine = create_engine(databaseUrl, echo=True)  # Crea el motor de la base de datos SQLite con echo=True para mostrar las consultas SQL en la consola

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # Crea una clase de sesión para interactuar con la base de datos

Session =sessionmaker(bind=engine)  # Crea una clase de sesión para interactuar con la base de datos

Base = declarative_base()  # Crea una clase base para los modelos de la base de datos