from fastapi import Header, HTTPException

from .database import SessionLocal

from .config import settings
import jwt

SECRET_KEY = settings.SECRET_KEY

ALGORITHM = settings.ALGORITHM

def decode(token):
    striped_token = token.replace("Bearer ", "")
    return jwt.decode(token, "secret", algorithm=ALGORITHM)

def encode():
    return jwt.encode({"some": "payload"}, "secret", algorithm=ALGORITHM)

def get_db():
    ''' Method for configure database '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
    
async def get_token_header(x_token: str = Header(...)):
    ''' Exemplo of header validation dependency '''
    payload = decode(x_token)
    username: str = payload.get("email")
    if username == None:
        raise HTTPException(status_code=403, detail="Unauthorized")


async def get_query_token(token: str):
    ''' Exemplo of header validation dependency '''
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")

