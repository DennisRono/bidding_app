
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from deps import get_current_user
import models
import schemas


router = APIRouter(prefix="/products")

@router.post('/new', status_code=status.HTTP_201_CREATED)
def register_user(db:Session = Depends(get_db), user: models.UserBase = Depends(get_current_user)):
    pass

