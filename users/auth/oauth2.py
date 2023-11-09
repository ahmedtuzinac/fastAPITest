# --------- DEPENDENCIES ---------- # 
from datetime import datetime, timedelta
from fastapi import (Depends, HTTPException,
                     status, APIRouter)
from fastapi.security import (OAuth2PasswordBearer,
                              OAuth2PasswordRequestForm)
from jose import JWTError, jwt
from typing import Annotated
from sqlalchemy.orm import Session 

# -------- PROJECT imports -------- #
from users.auth.schemasToken import (Token,
                                     TokenData)
from core.database import get_db
from core import models
from users import utils

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    
                                     
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(
   data: dict,
   expires_delta: timedelta | None = None
   ):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow()\
                 + expires_delta
    else:
        expire = datetime.utcnow()\
                 + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    
    return encoded_jwt

async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = db.query(models.User)\
           .filter(models.User.username==username)\
           .first()
    if user is None:
        raise credentials_exception
    return user

def authenticate_user(username, password, db):
    user = db.query(models.User)\
           .filter(models.User.username==username)\
           .first()
    if not user:
        return None
    if utils.verify_password(password, user.password):
        return user 
    
    
@router.post("/login", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

