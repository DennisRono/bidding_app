from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Numeric, text, JSON
from sqlalchemy.orm import relationship, mapped_column

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    bids = relationship("Bids", back_populates="bidder")

    def __repr__(self):
        return f'<User {self.full_name}>'

class Auctions(Base):
    __tablename__ = "auctions"

    id = Column(Integer, primary_key=True, nullable=False)
    auction_name = Column(String, nullable=False)
    auction_description = Column(String, nullable=False)
    start_time = Column(TIMESTAMP(timezone=True), nullable=False)
    end_time = Column(TIMESTAMP(timezone=True), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    products = relationship("Products", back_populates="auction")
    bids = relationship("Bids", back_populates="auction")

    def __repr__(self):
        return f'<Auction {self.auction_name}>'

class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=False)
    auction_id = Column(Integer, ForeignKey("auctions.id"), nullable=False)
    product_name = Column(String, nullable=False)
    product_image_urls = Column(JSON, nullable=False)
    product_description = Column(String, nullable=False)
    starting_price = Column(Numeric, nullable=False)
    end_time = Column(TIMESTAMP(timezone=True), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    auction = relationship("Auctions", back_populates="products")
    bids = relationship("Bids", back_populates="product")

    def __repr__(self):
        return f'<Product {self.product_name}>'

class Bids(Base):
    __tablename__ = "bids"

    id = Column(Integer, primary_key=True, nullable=False)
    auction_id = Column(Integer, ForeignKey("auctions.id"), nullable=False)
    bidder_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    bid_amount = Column(Numeric, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    auction = relationship("Auctions", back_populates="bids")
    bidder = relationship("Users", back_populates="bids")
    product = relationship("Products", back_populates="bids")

    def __repr__(self):
        return f'<Bid {self.bid_amount} by {self.bidder.full_name}>'
