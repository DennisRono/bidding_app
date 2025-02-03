from typing import List, Dict
from fastapi import HTTPException, Depends
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token
from sqlalchemy.orm import Session
from starlette import status
import models
import schemas
from fastapi import APIRouter
from database import get_db

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.get('/', response_model=List[schemas.CreateUser])
def fetch_users(db: Session = Depends(get_db)):
    user = db.query(models.Users).all()
    return  user

@router.post('/register', status_code=status.HTTP_201_CREATED, response_model=List[schemas.CreateUser])
def register_user(user_user:schemas.UserBase, db:Session = Depends(get_db)):
    new_user = models.Users(
        id = user_user.id,
        full_name = user_user.full_name,
        email = user_user.email,
        password = generate_password_hash(user_user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return [new_user]


@router.get('/{id}', response_model=schemas.CreateUser, status_code=status.HTTP_200_OK)
def get_one_user(id:int ,db:Session = Depends(get_db)):
    idv_user = db.query(models.Users).filter(models.Users.id == id).first()
    if idv_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The id: {id} you requested for does not exist")
    return idv_user

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:int, db:Session = Depends(get_db)):
    deleted_user = db.query(models.Users).filter(models.Users.id == id)
    if deleted_user.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id: {id} you requested for does not exist")
    deleted_user.delete(synchronize_session=False)
    db.commit()


@router.post('/login', status_code=status.HTTP_200_OK, response_model=Dict[str, schemas.LoginRespose])
def login_user(user:schemas.UserLogin, db:Session = Depends(get_db)):
    emailv_user = db.query(models.Users).filter(models.Users.email == user.email).first()
    if emailv_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The email: {user.email} you requested for does not exist")
    if not check_password_hash(emailv_user.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The password provided is wrong!")
    return schemas.LoginRespose.parse_obj({
        "access_token": create_access_token(identity=emailv_user.email),
        "refresh_token": create_refresh_token(identity=emailv_user.email)
    })
    
    