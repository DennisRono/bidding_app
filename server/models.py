from database import Base, get_db
from sqlalchemy import Column, Integer, String, TIMESTAMP, text

db = get_db()
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    def __repr__(self):
            return '<User %r>' % self.full_name
    
class Admins(Base):
     __tablename__ = "admins"

     id = Column(Integer, primary_key=True, nullable=False)
     full_name = Column(String, nullable=False)
     email = Column(String, nullable=False)
     password = Column(String, nullable=False)
     created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
 
     def __repr__(self):
            return '<Admins %r>' % self.full_name
    
class Products(Base):
     __tablename__ = "products"

     id = Column(Integer, primary_key=True, nullable=False)
     product_name = Column(String, nullable=False)
     product_description = Column(String, nullable=False)
     created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

     def __repr__(self):
            return '<Product %r>' % self.product_name
     
class Bids(Base):
     __tablename__ = "bids"

     id = Column(Integer, primary_key=True, nullable=False)
     bidder_id = db.ForeignKey
     created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

     def __repr__(self):
            return '<Bids %r>' % self.full_name
    