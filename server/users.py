from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
import models
import schemas
from fastapi import APIRouter
from database import get_db

router = APIRouter(prefix="/users")

@router.get('/', response_model=List[schemas.CreateUser])
def fetch_users(db: Session = Depends(get_db)):
    user = db.query(models.Users).all()
    return  user

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