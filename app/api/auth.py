from datetime import timedelta

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer

from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.schemas.auth import LoginSchema, RegisterSchema, Token
from app.services.auth_service import authenticate_user
from app.services.security_service import create_access_token, get_password_hash


router = APIRouter()

fake_users_db = [
    {
        "name": "johndoe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@router.post("/login")
async def login(
    form_data: LoginSchema,
) -> Token:
    user = authenticate_user(fake_users_db, form_data.email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect name or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@router.post("/register")
def register(user_data: RegisterSchema):  
    for user_data_db in fake_users_db:
        if(user_data_db['email'] == user_data.email):
            raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user_data.password)

    fake_users_db.append({
        "name": user_data.name,
        "email": user_data.email,
        "hashed_password": hashed_password,
    })

    return {"msg": "User registered successfully"} 