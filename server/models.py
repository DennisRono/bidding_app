import uuid
from database import Base
from sqlalchemy import TIMESTAMP, ForeignKey, Integer, Numeric, String, text, JSON
from sqlalchemy.orm import relationship, mapped_column

class Users(Base):
    __tablename__ = "users"

    id = mapped_column(
        String,
        unique=True,
        nullable=False,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )
    full_name = mapped_column(String, nullable=False)
    email = mapped_column(String, unique=True, nullable=False)
    password_hash = mapped_column(String, nullable=False)
    role = mapped_column(String, nullable=False)
    created_at = mapped_column(TIMESTAMP(timezone=True), server_default=text('now()'))

    bids = relationship("Bids", back_populates="bidder")

    def __repr__(self):
        return f'<User {self.full_name}>'

class Auctions(Base):
    __tablename__ = "auctions"

    id = mapped_column(
        String,
        unique=True,
        nullable=False,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )
    auction_name = mapped_column(String, nullable=False)
    auction_description = mapped_column(String, nullable=False)
    start_time = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    end_time = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    created_at = mapped_column(TIMESTAMP(timezone=True), server_default=text('now()'))

    products = relationship("Products", back_populates="auction")
    bids = relationship("Bids", back_populates="auction")

    def __repr__(self):
        return f'<Auction {self.auction_name}>'

class Products(Base):
    __tablename__ = "products"

    id = mapped_column(
        String,
        unique=True,
        nullable=False,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )
    auction_id = mapped_column(Integer, ForeignKey("auctions.id"), nullable=False)
    product_name = mapped_column(String, nullable=False)
    product_image_urls = mapped_column(JSON, nullable=False)
    product_description = mapped_column(String, nullable=False)
    starting_price = mapped_column(Numeric, nullable=False)
    end_time = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    created_at = mapped_column(TIMESTAMP(timezone=True), server_default=text('now()'))

    auction = relationship("Auctions", back_populates="products")
    bids = relationship("Bids", back_populates="product")

    def __repr__(self):
        return f'<Product {self.product_name}>'

class Bids(Base):
    __tablename__ = "bids"

    id = mapped_column(
        String,
        unique=True,
        nullable=False,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )
    auction_id = mapped_column(Integer, ForeignKey("auctions.id"), nullable=False)
    bidder_id = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = mapped_column(Integer, ForeignKey("products.id"), nullable=False)
    bid_amount = mapped_column(Numeric, nullable=False)
    created_at = mapped_column(TIMESTAMP(timezone=True), server_default=text('now()'))

    auction = relationship("Auctions", back_populates="bids")
    bidder = relationship("Users", back_populates="bids")
    product = relationship("Products", back_populates="bids")

    def __repr__(self):
        return f'<Bid {self.bid_amount} by {self.bidder.full_name}>'
