from typing import List
from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from starlette import status
from datetime import datetime

import models
import schemas
from database import get_db

bid_router = APIRouter(prefix="/bid")

@bid_router.get('/{id}', response_model=List[schemas.BidResponse], status_code=status.HTTP_200_OK)
def get_all_bids_for_one_user(id: int, db: Session = Depends(get_db)):
    bids = db.query(models.Bids).filter(models.Bids.user_id == id).all()
    if not bids:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No bids found for this user")
    return bids

@bid_router.post('/place', response_model=schemas.BidResponse, status_code=status.HTTP_201_CREATED)
def place_bid(bid: schemas.BidCreate, db: Session = Depends(get_db)):
    product = db.query(models.Products).filter(models.Products.id == bid.product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    if datetime.utcnow() > product.end_time:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bidding time has elapsed for this product")
    
    last_bid = db.query(models.Bids).filter(models.Bids.product_id == bid.product_id).order_by(models.Bids.bid_amount.desc()).first()
    if last_bid and bid.bid_amount <= last_bid.bid_amount:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bid amount must be higher than the current highest bid")
    
    new_bid = models.Bids(
        auction_id=product.auction_id,
        product_id=bid.product_id,
        bidder_id=bid.user_id,
        bid_amount=bid.bid_amount
    )
    db.add(new_bid)
    db.commit()
    db.refresh(new_bid)
    return new_bid
