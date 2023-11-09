# --------- DEPENDENCIES ---------- # 
from fastapi import FastAPI

# -------- PROJECT imports -------- #
from users import urlsUsers
from core import models
from core.database import engine 
from users.auth import oauth2
from posts import urlsPosts


app = FastAPI()
app.include_router(urlsUsers.router)
app.include_router(urlsPosts.router)
app.include_router(oauth2.router)
