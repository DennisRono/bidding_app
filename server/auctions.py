from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
import models
import schemas
from fastapi import APIRouter
from database import get_db
from deps import get_current_user

auction_router = APIRouter(prefix="/auction")

@auction_router.post('/create', status_code=status.HTTP_201_CREATED, response_model=schemas.AuctionBase)
def create_auction(auction: schemas.AuctionBase, db: Session = Depends(get_db), user = Depends(get_current_user)):
    new_auction = models.Auctions(
        auction_name=auction.auction_name,
        auction_description=auction.auction_description,
        start_time=auction.start_time,
        end_time=auction.end_time
    )
    db.add(new_auction)
    db.commit()
    db.refresh(new_auction)
    return new_auction

@auction_router.get('/', response_model=List[schemas.AuctionBase])
def get_all_auctions(db: Session = Depends(get_db)):
    auctions = db.query(models.Auctions).all()
    return auctions

@auction_router.put('/update/{auction_id}', response_model=schemas.AuctionBase)
def update_auction(auction_id: int, auction: schemas.AuctionBase, db: Session = Depends(get_db), user = Depends(get_current_user)):
    existing_auction = db.query(models.Auctions).filter(models.Auctions.id == auction_id).first()
    if not existing_auction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Auction not found")
    existing_auction.auction_name = auction.auction_name
    existing_auction.auction_description = auction.auction_description
    existing_auction.start_time = auction.start_time
    existing_auction.end_time = auction.end_time
    db.commit()
    db.refresh(existing_auction)
    return existing_auction

@auction_router.delete('/delete/{auction_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_auction(auction_id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    existing_auction = db.query(models.Auctions).filter(models.Auctions.id == auction_id).first()
    if not existing_auction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Auction not found")
    db.delete(existing_auction)
    db.commit()
    return
