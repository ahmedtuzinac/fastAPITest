from pydantic import BaseModel

from users.schemasUser import User

class PostBaseModel(BaseModel):
    
    title: str 
    content: str

class PostReadModel(BaseModel):
    
    id: int
    title: str 
    content: str
    owner: User 
    
    class Config:
        from_attributes = True