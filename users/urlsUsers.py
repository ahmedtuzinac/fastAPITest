# --------- DEPENDENCIES ---------- # 
from fastapi import (APIRouter, Depends)
from sqlalchemy.orm import Session 

# -------- PROJECT imports -------- #
from core.database import get_db
from users import views
from users.schemasUser import User, UserRegister
from users.auth.oauth2 import get_current_user

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.get('/',
            response_model=list[User])
def get_users(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    print(current_user)
    return views.get_users_db(db=db)

@router.post('/',
             response_model=User)
def register(user_data: UserRegister,
             db: Session = Depends(get_db)):
    return views.create_user_db(
        user_data=user_data,
        db=db
    )





