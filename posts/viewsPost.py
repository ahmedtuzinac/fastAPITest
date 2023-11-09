# --------- DEPENDENCIES ---------- # 


# -------- PROJECT imports -------- #
from core import models


def get_posts_db(**kwargs):
    db = kwargs.get('db')
    return db.query(models.Post).all()

def create_post_db(**kwargs):
    user = kwargs.get('user')
    post_data = kwargs.get('post_data')
    db = kwargs.get('db')
    
    new_post = models.Post(
        **post_data.dict(),
        owner_id = user.id
    )
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post 
    