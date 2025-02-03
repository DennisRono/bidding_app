from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text


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

     def __repr__(self):
            return '<User %r>' % self.full_name
    
class Products(Base):
     __tablename__ = "products"

     id = Column(Integer, primary_key=True, nullable=False)

     def __repr__(self):
            return '<User %r>' % self.full_name
     
class Bids(Base):
     __tablename__ = "bids"

     id = Column(Integer, primary_key=True, nullable=False)

     def __repr__(self):
            return '<User %r>' % self.full_name
    