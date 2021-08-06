from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base

# Our ORM (object relational mapping) models that are needed for
# the program to interface with the database

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


# The User class
class User(Base):
    # corresponds the users table in our DB
    __tablename__ = "users"

    # these properties are columns in the DB
    # our id is the primary key and is used as an index
    id = Column(Integer, primary_key=True, index=True)
    # the email must be unique and is also used as an index
    email = Column(String, unique=True, index=True)
    # the 'hashed' password is saved as a string
    hashed_password = Column(String)
    # is_active is an under-utilized boolean
    is_active = Column(Boolean, default=True)
    # here we define an ORM relationship with the WishlistItem class
    items = relationship("WishlistItem", back_populates="owner")

# The WishlistItem class
class WishlistItem(Base):
    # corresponds with the wishlist_items table
    __tablename__ = "wishlist_items"

    # all our tables have autoincremented numerical IDs as a primary key
    id = Column(Integer, primary_key=True, index=True)
    # The other properties are pretty straightforward
    name = Column(String)
    description = Column(String)
    link = Column(String)
    price = Column(Float)
    # the foreign key is a strict relationship to column in another table
    owner_id = Column(Integer, ForeignKey("users.id"))
    # The counterpart to the items relationship in the Users table
    owner = relationship("User", back_populates="items")