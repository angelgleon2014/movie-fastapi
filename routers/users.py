from fastapi import APIRouter
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse, JSONResponse
from user_jwt import createToken

routerAuth = APIRouter()

class User(BaseModel):
    email: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=3, max_length=50)

@routerAuth.post('/login', tags=['Authentication'])
def login(user: User):
    if user.email == 'stringddd@aaa.com' and user.password == '123':
        token :str = createToken(user.model_dump())
        # print(token)
        return JSONResponse(content=token)
    return JSONResponse(content={"message": "Invalid credentials"}, status_code=401)
