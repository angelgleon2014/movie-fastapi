from fastapi import Path, Query, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional
from user_jwt import validateToken
from fastapi.security import HTTPBearer as HHTTPBearer
from bd.database import Session
from models.movie import Movie as ModelMovie
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter

routerMovie = APIRouter()

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default='Titulo de la pelicula', min_length=5, max_length=60) # Validacion del título que debe tener al menos 3 caracteres y máximo 60
    overview: str = Field(default='Descripcion de la pelicula', min_length=15, max_length=60)
    year: int = Field(default=2023, ge=1900, le=2100)  # Validación del año que debe estar entre 1900 y 2100
    rating: float = Field(default=1, ge=1, le=10)  # Validación de la calificación que debe estar entre 0.0 y 10.0
    category: str = Field(default='Aqui va la categoria', min_length=3, max_length=30)  # Validación de la categoría que debe tener al menos 3 caracteres y máximo 30
    created_at: datetime = Field(default_factory=datetime.now)  # Ahora es datetime
    updated_at: Optional[datetime] = None  # También datetime, opcional
    is_active : bool = Field(default=True)  # Indica si la película está activa o no, por defecto es True

class BearerJWT(HHTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validateToken(auth.credentials)  # Validamos el token
        if data['email'] != 'stringddd@aaa.com':
            raise HTTPException(status_code=403, detail="Credenciales incorrectas.")


@routerMovie.get('/movies', tags=['Get Movies'], status_code=200, dependencies=[Depends(BearerJWT())])  # Dependencia para autenticar el token JWT
def get_movies():
    db = Session()
    movies_db = db.query(ModelMovie).all()    
    return JSONResponse(content=jsonable_encoder(movies_db), status_code=200)  # Retorna la lista de películas en formato JSON con código de estado 200


@routerMovie.get('/movies/{id}', tags=['Get Movie'], status_code=200)
def get_movie(id: int = Path(ge=1, description="ID de la película a consultar")):
    db = Session()
    movie = db.query(ModelMovie).filter(ModelMovie.id == id).first()
    if movie:
        return JSONResponse(content=jsonable_encoder(movie), status_code=200)
    return JSONResponse(content={"message": "Película no encontrada"}, status_code=404)


@routerMovie.get('/movies/', tags=['Get Movies By Category'], status_code=200)
def get_movies_by_category(category: str = Query(..., min_length=3, max_length=30, description="Categoría de la película a buscar")):
    db = Session()
    movies_db = db.query(ModelMovie).filter(ModelMovie.category.ilike(f"%{category}%")).all()
    if movies_db:
        return JSONResponse(content=jsonable_encoder(movies_db), status_code=200)
    return JSONResponse(content={"message": "No se encontraron películas para esta categoría"}, status_code=404)


@routerMovie.post('/movies', tags=['Create Movie'], status_code=201)
def create_movie(movie : Movie):
    db = Session()
    if not movie.created_at:
        movie.created_at = datetime.now()
    newMovie = ModelMovie(**movie.model_dump())
    db.add(newMovie)
    db.commit()
    # Usar jsonable_encoder para serializar todo el objeto
    movie_dict = jsonable_encoder(movie)
    return JSONResponse(content={"message": "Movie created successfully", "movie": movie_dict}, status_code=201)


@routerMovie.put('/movies/{id}', tags=['Update Movie'], status_code=200)
def update_movie(id: int, movie: Movie):
    db = Session()
    movie_db = db.query(ModelMovie).filter(ModelMovie.id == id).first()
    if not movie_db:
        return JSONResponse(content={"message": "Película no encontrada"}, status_code=404)
    # Actualizar los campos
    movie_data = movie.model_dump(exclude_unset=True)
    for key, value in movie_data.items():
        setattr(movie_db, key, value)
    movie_db.updated_at = datetime.now()
    db.commit()
    db.refresh(movie_db)
    return JSONResponse(content={"message": "Película actualizada correctamente", "movie": jsonable_encoder(movie_db)}, status_code=200)



@routerMovie.delete('/movies/{id}', tags=['Delete Movie'], status_code=200)
def delete_movie(id: int):
    db = Session()
    movie_db = db.query(ModelMovie).filter(ModelMovie.id == id).first()
    if not movie_db:
        return JSONResponse(content={"message": "Película no encontrada"}, status_code=404)
    db.delete(movie_db)
    db.commit()
    return JSONResponse(content={"message": "Película eliminada correctamente"}, status_code=200)