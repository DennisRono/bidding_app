from typing import List, Dict
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
from helpers.auth import create_access_token, create_refresh_token, get_hashed_password, verify_password
import models
import schemas
from fastapi import APIRouter
from database import get_db

router = APIRouter(prefix="/auth")

@router.post('/register', status_code=status.HTTP_201_CREATED, response_model=List[schemas.CreateUser])
def register_user(user_user:schemas.UserBase, db:Session = Depends(get_db)):
    new_user = models.Users(
        id = user_user.id,
        full_name = user_user.full_name,
        email = user_user.email,
        password = get_hashed_password(user_user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return [new_user]


@router.post('/login', status_code=status.HTTP_200_OK, response_model=schemas.LoginRespose)
def login_user(user:schemas.UserLogin, db:Session = Depends(get_db)):
    emailv_user = db.query(models.Users).filter(models.Users.email == user.email).first()
    if emailv_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The email: {user.email} you requested for does not exist")
    if not verify_password(user.password, emailv_user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The password provided is wrong!")
    return schemas.LoginRespose.parse_obj({
        "access_token": create_access_token(identity=emailv_user.email),
        "refresh_token": create_refresh_token(identity=emailv_user.email)
    })
    
router.post('/access-token', status_code=status.HTTP_200_OK,)
def is_token_valid(token: schemas.UserLogin, db:Session = Depends(get_db)):
    pass