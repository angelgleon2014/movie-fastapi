from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from bd.database import engine, Base
from routers.movie import routerMovie
from routers.users import routerAuth

app = FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application.",
    version="0.0.1"
)

app.include_router(routerMovie)
app.include_router(routerAuth)

Base.metadata.create_all(bind=engine) # crea las tablas en la base de datos si no existen

@app.get("/", tags=["Inicio"])
def read_root():
    return HTMLResponse('<h2>Welcome to My FastAPI Application</h2><p>This is a sample application to demonstrate FastAPI features.</p>')
