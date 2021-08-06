from typing import List, Optional

from pydantic import BaseModel

# The schema is used for validating that expected properties
# are present and of the expected type
class ItemBase(BaseModel):
    name: str
    # we can designate properties as optional with a default
    description: Optional[str] = None
    link: str
    price: float


class ItemCreate(ItemBase):
    # https://www.programiz.com/python-programming/pass-statement
    # the pass statement is placeholder and does not do anything
    # this code was added as part of the tutorial and likely meant to be
    # expanded on in advanced tutorials 
    pass

# The Item class extends ItemBase and is used to return Item with all of its properties
class Item(ItemBase):
    id: int
    owner_id: int

    # Pydantic's orm_mode will allow reading data even when it's
    # not a dictionary allowing compatibility with ORMs such as SQLAlchemy
    class Config:
        orm_mode = True

# The UserBase class establishes the minimum for a User, the email
class UserBase(BaseModel):
    email: str

# A User must be created with a password
class UserCreate(UserBase):
    password: str

# The returned User has items attacehd but does not return the password
class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True