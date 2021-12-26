from typing import ContextManager
from sqlalchemy.sql.sqltypes import Boolean, Integer
from .database import Base
from sqlalchemy import Column, String

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key= True, nullable= False)
    title  = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True)    