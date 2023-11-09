# --------- DEPENDENCIES ---------- # 
from fastapi import HTTPException, status

# -------- PROJECT imports -------- #
from core import models
from users import utils


def get_users_db(db):
    return db.query(models.User).all()

def create_user_db(db, user_data):
    
    user = db.query(models.User).\
           filter(models.User.username==user_data.username).first()

    if user:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail='username already exists'
        )
    
    user = models.User(
        **user_data.dict()
    )
    user.password = utils.get_password_hash(
        user_data.password
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user