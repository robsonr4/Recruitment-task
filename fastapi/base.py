from pydantic import BaseModel, Field

class LoginBase(BaseModel):
    username: str = Field(default=None, description="User's username")
    password: str = Field(default=None, description="User's password")

class MailBase(BaseModel):
    email: str = Field(default=None, description="User's email")

class UserBase(LoginBase, MailBase):
    firstname: str | None = Field(default=None, description="User's first name")
    lastname: str | None = Field(default=None, description="User's last name")

class ResetPasswordBase(BaseModel):
    password: str
    confirm_password: str

class ResetPasswordTokenBase(BaseModel):
    token: str