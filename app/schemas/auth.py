from pydantic import BaseModel, EmailStr, field_validator
import re

class LoginSchema(BaseModel):
    email: EmailStr
    password: str

class RegisterSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

    @field_validator('name')
    def validate_username(cls,v): 
            if len(v) > 20:
                raise ValueError('name must be at most 20 characters long')
            if len(v) < 3:
                raise ValueError('name must be at least 3 characters long')
            if not re.match(r'^[a-zA-Z ]+$', v):
                raise ValueError('Name can only contain letters and spaces (no numbers or special characters)')
            return v

    @field_validator('password')
    def validate_password_strength(cls,v): 
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not re.search(r"[A-Z]",v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r"[a-z]", v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r"\d", v):
            raise ValueError('Password must contain at least one number')
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", v):
            raise ValueError('Password must contain at least one special character')
        return v

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    name: str | None = None


class User(BaseModel):
    name: str
    email: str

class UserInDB(User):
    hashed_password: str