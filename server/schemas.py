from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from datetime import datetime

class UserBase(BaseModel):
    id: str
    full_name: str
    email: str
    role: str
    password: str

    model_config = ConfigDict(from_attributes=True)

class SystemUser(BaseModel):
    id: str
    full_name: str
    email: str
    role: str
    password: str

    model_config = ConfigDict(from_attributes=True)
class UserLogin(BaseModel):
    email: str
    password: str

    model_config = ConfigDict(from_attributes=True)

class TokData(BaseModel):
    exp: int
    sub: str

    model_config = ConfigDict(from_attributes=True)

class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str

    model_config = ConfigDict(from_attributes=True)

class CreateUser(UserBase):
    id: str
    full_name: str
    email: str
    role: str
    created_at: datetime

class NewProduct(BaseModel):
    id: str
    product_name: str
    product_image_urls: list[str]
    product_description: str
    starting_price: int
    end_time: datetime


class TokenRefresh(BaseModel):
    refresh_token: str

    model_config = ConfigDict(from_attributes=True)

class TokenResponse(BaseModel):
    access_token: str

    model_config = ConfigDict(from_attributes=True)

class BidCreate(BaseModel):
    product_id: int
    user_id: int
    bid_amount: Decimal

    model_config = ConfigDict(from_attributes=True)

class BidResponse(BaseModel):
    id: str
    product_id: int
    user_id: int
    bid_amount: Decimal
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AuctionBase(BaseModel):
    auction_name: str
    auction_description: str
    start_time: datetime
    end_time: datetime

    model_config = ConfigDict(from_attributes=True)