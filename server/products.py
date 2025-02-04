
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from deps import get_current_user
import models
import schemas


product_router = APIRouter(prefix="/products")

# user should have role=admin to create a product
@product_router.post('/new', status_code=status.HTTP_201_CREATED)
def create_new_product(product:schemas.NewProduct, db:Session = Depends(get_db), user = Depends(get_current_user)):
    print(user, product)
    new_product = models.Products(
        id = product.id,
        product_name = product.product_name,
        product_image_urls = product.product_image_urls,
        product_description = product.product_description,
        starting_price = product.starting_price,
        end_time = product.end_time
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

# return all products
@product_router.get('/', status_code=status.HTTP_200_OK)
def fetch_all_products(db:Session = Depends(get_db)):
    all_products = db.query(models.Products).all()
    return  all_products