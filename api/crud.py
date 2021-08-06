from sqlalchemy.orm import Session

from . import models, schemas

# This is one of the main files of our API
# Here we handle the CRUD (create, read, update, delete) operations

# used by GET /users/{id}
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# used by POST /users/
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# used by GET /users/
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# used by POST /users/
def create_user(db: Session, user: schemas.UserCreate):
    # because we don't have a mechanism for hashing passwords...
    fake_hashed_password = user.password + "notreallyhashed"
    # create the user per the model
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    # db operations to create the user in the DB
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# used by GET /items/
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.WishlistItem).offset(skip).limit(limit).all()

# used by POST /users/{id}/items/
def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    # create the item model
    db_item = models.WishlistItem(**item.dict(), owner_id=user_id)
    # add the item to the database
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item