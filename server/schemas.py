from typing import Dict
from pydantic import BaseModel

class UserBase(BaseModel):
    id: int
    full_name: str
    email: str
    password: str

    class Config:
        orm_mode = True

class UserLogin():
    email: str
    password: str
    class Config:
        orm_mode = True

class LoginRespose():
    __root__: Dict[str, str]

    class Config:
        orm_mode = True

class CreateUser(UserBase):
    class Config:
        orm_mode = True