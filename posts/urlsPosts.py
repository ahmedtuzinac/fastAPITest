# --------- DEPENDENCIES ---------- # 
from fastapi import (APIRouter, Depends)
from sqlalchemy.orm import Session

# -------- PROJECT imports -------- #
from core.database import get_db
from users.auth.oauth2 import get_current_user
from posts import viewsPost
from posts.schemasPost import (PostBaseModel,
                               PostReadModel)



router = APIRouter(
    prefix='/posts',
    tags=['posts']
)

@router.get(
    '/', response_model=list[PostReadModel]
)
def get_posts(db: Session = Depends(get_db)):
    return viewsPost.get_posts_db(db=db)

@router.post(
    '/', response_model=PostReadModel
)
def create_post(
    post_data: PostBaseModel,
    user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return viewsPost.create_post_db(
        user=user,
        post_data=post_data,
        db=db
    )
    