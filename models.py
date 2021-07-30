from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base

### Our ORM models

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


# # users
# class User(Base):
#     # define our table name
#     __tablename__ = "users"
#     # define the columns, their types, and attributes
#     id = Column(Integer, primary_key=True, index=True)# there should be one primary key per table
#     email = Column(String, unique=True, index=True)# a unique identifier can be an index
#     hashed_password = Column(String)
#     first_name = Column(String)
#     last_name = Column(String)
#     # wish_list populates wish list items where the requester is this user
#     wish_list = relationship("WishList", back_populates="requester")


# # wishlist items
# class WishList(Base):
#     __tablename__ = "wish_list"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     description = Column(String)
#     requester_id = Column(Integer, ForeignKey("users.id"))
#     item_link = Column(String)
#     item_price = Column(Float)
#     requester = relationship("User", back_populates="wish_list")