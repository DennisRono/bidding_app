from typing import List, Dict
import uuid
from fastapi import HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette import status
from helpers.auth import create_access_token, create_refresh_token, get_hashed_password, verify_password, JWT_REFRESH_SECRET_KEY, ALGORITHM
import models
import schemas
from fastapi import APIRouter
from database import get_db
from jose import jwt, JWTError

auth_router = APIRouter(prefix="/auth")

@auth_router.post('/register', status_code=status.HTTP_201_CREATED, response_model=List[schemas.CreateUser])
def register_user(user_user:schemas.UserBase, db:Session = Depends(get_db)):
    emailv_user = db.query(models.Users).filter(models.Users.email == user_user.email).first()
    if emailv_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    try:
        new_user = models.Users(
            id=str(uuid.uuid4()),
            full_name=user_user.full_name,
            email=user_user.email,
            role=user_user.role,
            password_hash=get_hashed_password(user_user.password)
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return [new_user]


@auth_router.post('/login', status_code=status.HTTP_200_OK, response_model=schemas.LoginResponse)
def login_user(user:schemas.UserLogin, db:Session = Depends(get_db)):
    emailv_user = db.query(models.Users).filter(models.Users.email == user.email).first()
    if emailv_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The email: {user.email} you requested for does not exist")
    if not verify_password(user.password, emailv_user.password_hash):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The password provided is wrong!")
    return schemas.LoginResponse.parse_obj({
        "user": jsonable_encoder(emailv_user),
        "access_token": create_access_token(emailv_user.email),
        "refresh_token": create_refresh_token(emailv_user.email)
    })


@auth_router.post('/refresh', status_code=status.HTTP_200_OK, response_model=schemas.TokenResponse)
def refresh_access_token(token: schemas.TokenRefresh):
    try:
        payload = jwt.decode(token.refresh_token, JWT_REFRESH_SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Invalid token payload"
            )
        new_access_token = create_access_token(email)
        return schemas.TokenResponse(access_token=new_access_token)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid refresh token"
        )
    