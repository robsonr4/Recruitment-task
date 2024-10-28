from typing import Union, List, Annotated
from fastapi import FastAPI, HTTPException, Depends, Response, status, Body
from pydantic import BaseModel, Field
import models
from db import SessionLocal, engine
from sqlalchemy.orm import Session
import smtplib
from email.mime.text import MIMEText
from base import LoginBase, MailBase, UserBase, ResetPasswordBase, ResetPasswordTokenBase
from dotenv import load_dotenv
import constants as const

load_dotenv()

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/login/", status_code=status.HTTP_200_OK, description=const.LOGIN_POST_DESC)
async def login(user: Annotated[LoginBase, Body(embed=True)], db: db_dependency):
    """Login user
    
    BODY
    ----
    username: str
        User's username
    password: str
        User's password
    
    RETURNS
    -------
    message: str
        Login successful
    
    Raises:
    HTTPException: 404
        The user does not exist
    HTTPException: 401
        The password is incorrect
    """

    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    # check len
    elif db_user.hashed_password != user.password:
        raise HTTPException(status_code=401, detail="Invalid password")
    return {"message": "Login successful"}
    

@app.post("/register/")
async def register(user: UserBase, db: db_dependency):
    """Register user
    
    BODY
    ----
    username: str
        User's username
    password: str
        User's password
    email: str
        User's email
    firstname: str
        User's first name
    lastname: str
        User's last name
    
    RETURNS
    -------
    message: str
        User created

    Raises:
    HTTPException: 404
        The user with this email or username already exists
    """
    db_user = models.User(firstname=user.firstname, lastname=user.lastname, username=user.username, hashed_password=user.password, email=user.email)
    db.add(db_user)

    try:
        db.commit()
    except:
        raise HTTPException(status_code=404, detail="User with this email or username already exists")
    
    db.refresh(db_user)
    return {"message": "User created"}

@app.post("/reset-password-mail/")
async def reset_password_mail(user: MailBase, db: db_dependency):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User with this email does not exist")
    
    return NotImplemented


@app.post("/reset-password/")
async def reset_password(user: ResetPasswordBase):
    return "Password reseted"

@app.get("/reset-password-token/")
async def reset_password_token(user: ResetPasswordTokenBase):
    return "Existing and valid token"

@app.get("/main_page/")
async def main_page():
    return "Main page"

