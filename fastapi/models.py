from sqlalchemy import String, Column, Integer, Boolean, DATE
from db import Base

class User(Base):
    """User model
    
    Fields:
    id: int
    firstname: str
    lastname: str
    username: str
    email: str
    password: str
    reset_password_token: str | None
    reset_password_token_expires: date | None"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    reset_password_token = Column(String, nullable=True)
    reset_password_token_expires = Column(DATE, nullable=True)




