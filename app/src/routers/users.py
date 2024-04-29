from typing import List,Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer,HTTPAuthorizationCredentials, HTTPBearer 

from sqlalchemy.orm import Session

from ..dependencies import get_db

from ..domain.user import service, schemas


router = APIRouter(tags=["users"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
security = HTTPBearer()

credentialDep  =  Annotated[HTTPAuthorizationCredentials, Depends(security)]
db_session      = Annotated[Session, Depends(get_db)]


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, credentials: credentialDep, db: db_session):
    db_user = service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return service.create_user(db=db, user=user)

@router.get("/users/", response_model=List[schemas.User]) 
def read_users(credentials: credentialDep, db: db_session, skip: int = 0, limit: int = 100):
    users = service.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: db_session):
    db_user = service.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(user_id: int, item: schemas.ItemCreate, db: db_session):
    return service.create_user_item(db=db, item=item, user_id=user_id)
