from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application.",
    version="0.0.1"
)

@app.get("/", tags=["Inicio"])
def read_root():
    # return {"Hello": "World"}
    return HTMLResponse('<h2>Welcome to My FastAPI Application</h2><p>This is a sample application to demonstrate FastAPI features.</p>')

movies = [
    {
        'id': 1,
        "title": "El Padrino",
        "overview": "El Padrino es una película de 1972 dirigida por Francis Ford Coppola",
        "year": 1972,
        "rating": 9.2,
        "category": "Crimen"
    }
]


@app.get('/movies', tags=['Get Movies'])
def get_movies():
    return movies


@app.get('/movies/{id}', tags=['Get Movie'])
def get_movie(id: int):
    for item in movies:
        if item['id'] == id:
            return item
    return [{"message": "Movie not found"}]

@app.get('/movies/', tags=['Get Movies By Category'])
def get_movies_by_category(category: str):
    filtered_movies = [movie for movie in movies if movie['category'].lower() == category.lower()]
    if filtered_movies:
        return filtered_movies
    return [{"message": "No movies found for this category"}]

@app.post('/movies', tags=['Create Movie'])
def create_movie(
    id: int = Body(),
    title: str = Body(),
    overview: str = Body(),
    year: int = Body(),
    rating: float = Body(),
    category: str = Body()
):
    new_movie = {
        'id': id,
        'title': title,
        'overview': overview,
        'year': year,
        'rating': rating,
        'category': category
    }
    movies.append(new_movie)
    return {"message": "Movie created successfully", "movie": new_movie}

@app.put('/movies/{id}', tags=['Update Movie'])
def update_movie(
    id: int,
    title: str = Body(None),
    overview: str = Body(None),
    year: int = Body(None),
    rating: float = Body(None),
    category: str = Body(None)
):
    for movie in movies:
        if movie['id'] == id:
            if title is not None:
                movie['title'] = title
            if overview is not None:
                movie['overview'] = overview
            if year is not None:
                movie['year'] = year
            if rating is not None:
                movie['rating'] = rating
            if category is not None:
                movie['category'] = category
            return {"message": "Movie updated successfully", "movie": movie}
    return {"message": "Movie not found"}

@app.delete('/movies/{id}', tags=['Delete Movie'])
def delete_movie(id: int):
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return {"message": "Movie deleted successfully"}
    return {"message": "Movie not found"}