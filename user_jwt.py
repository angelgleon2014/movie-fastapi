import jwt

def createToken(data :dict):
    token : str = jwt.encode(payload=data, key='misecret', algorithm='HS256')
    return token

""" def validateToken(token: str):
    try:
        decoded_data = jwt.decode(token, key='misecret', algorithms=['HS256'])
        return decoded_data
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}
    except Exception as e:
        return {"error": str(e)}  # Captura cualquier otra excepción y devuelve el mensaje de error """

def validateToken(token: str) -> dict:
    data : dict = jwt.decode(token, key='misecret', algorithms=['HS256'])
    return data
    
