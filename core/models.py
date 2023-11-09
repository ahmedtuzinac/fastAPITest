# --------- DEPENDENCIES ---------- # 
from datetime import datetime
from sqlalchemy import (Column, Integer,
                        String, Boolean,
                        DateTime, ForeignKey)
from sqlalchemy.orm import relationship

# -------- PROJECT imports -------- #
from core.database import Base

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer,
                primary_key=True)
    
    title = Column(String,
                   nullable=False)
    
    content = Column(String,
                     nullable=False)
    
    created = Column(DateTime,
                     default=datetime.utcnow)
    
    phone_number = Column(Integer, nullable=True)
    
    owner_id = Column(
        Integer,
        ForeignKey(
            'users.id',
            ondelete='CASCADE'
        )
    )
    owner = relationship(
        'User'
    )
    
    
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer,
                primary_key=True)
    username = Column(String,
                      nullable=False,
                      unique=True)
    password = Column(String,
                      nullable=False)
    
   

                     
    