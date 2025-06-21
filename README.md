# 🎬 My FastAPI Application

¡Bienvenido a **My FastAPI Application**!  
Este proyecto es una API RESTful desarrollada con [FastAPI](https://fastapi.tiangolo.com/) que permite gestionar una base de datos de películas y usuarios, implementando autenticación JWT y operaciones CRUD completas.

---

## 🚀 Características principales

- **CRUD de Películas:**  
  Crea, consulta, actualiza y elimina películas fácilmente.

- **Búsqueda avanzada:**  
  Filtra películas por categoría o por ID.

- **Autenticación JWT:**  
  Acceso seguro a los endpoints protegidos mediante tokens JWT.

- **Validaciones robustas:**  
  Todos los campos de entrada están validados con Pydantic.

- **Fechas automáticas:**  
  Los registros incluyen fecha de creación y actualización gestionadas automáticamente.

---

## 🛠️ Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [SQLite](https://www.sqlite.org/index.html) (por defecto, puedes cambiar el motor)
- [JWT](https://jwt.io/) para autenticación

---

## 📦 Estructura del proyecto

```
newfastapi/
├── bd/
│   └── database.py
├── models/
│   └── movie.py
├── routers/
│   ├── movie.py
│   └── users.py
├── main.py
└── README.md
```

---

## 🔐 Autenticación

Para acceder a los endpoints protegidos (por ejemplo, `/movies`), primero debes autenticarte usando el endpoint `/login`:

```json
POST /login
{
  "email": "stringddd@aaa.com",
  "password": "123"
}
```
Obtendrás un token JWT que deberás incluir en el header `Authorization` como `Bearer <token>` en tus siguientes peticiones.

---

## 📚 Endpoints principales

- `POST /login` — Obtén tu token JWT.
- `GET /movies` — Lista todas las películas (requiere autenticación).
- `GET /movies/{id}` — Consulta una película por su ID.
- `GET /movies/?category=Acción` — Busca películas por categoría.
- `POST /movies` — Crea una nueva película.
- `PUT /movies/{id}` — Actualiza una película existente.
- `DELETE /movies/{id}` — Elimina una película.

---

## ⚡ Ejecución rápida

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tuusuario/newfastapi.git
   cd newfastapi
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta el servidor:**
   ```bash
   uvicorn main:app --reload
   ```

4. **Explora la documentación interactiva:**
   - [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!  
Puedes abrir issues, enviar pull requests o proponer mejoras.

---

## 📝 Licencia

Este proyecto está bajo la licencia MIT.

---

**¡Gracias por visitar este proyecto! Si te resulta útil, no olvides darle una ⭐ en GitHub.**
