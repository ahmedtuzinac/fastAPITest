from pydantic import BaseModel


class User(BaseModel):
    
    id: int 
    username: str
    
    class Config:
        from_attributes = True

class UserRegister(BaseModel):
    
    username: str 
    password: str  