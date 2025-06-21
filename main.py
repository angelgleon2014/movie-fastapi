from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from bd.database import engine, Base
from routers.movie import routerMovie
from routers.users import routerAuth
import uvicorn
import os

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


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Obtiene el puerto del entorno o usa 8000 por defecto
    uvicorn.run(app, host="0.0.0.0", port=port)
    # uvicorn.run("main:app", host="0.0.0.0", port=port)