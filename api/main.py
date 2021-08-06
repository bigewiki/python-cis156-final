from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

# This is the primary file of our API

# Initialize our models
models.Base.metadata.create_all(bind=engine)

# Alias app
app = FastAPI()

# Dependency for working with SQLite
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST /users/ route
# this will create a new user
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # first check if the user exists
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        # 409 is the HTTP status code for conflict
        raise HTTPException(status_code=409, detail="Email already registered")
    # create the user
    return crud.create_user(db=db, user=user)

# GET /users/
# This returns all users with their wishlist items
@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # fetch and return the users
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# GET /users/{id}
# Returns the user with the specified ID
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    # fetch and return the singular user
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        # if user is missing return a 404 Not Found
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# POST /users/{id}/items
# With a JSON request body create the item for the specified user
@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    # custom exception handling if the user input bad params
    try:
        # try to create the item
        return crud.create_user_item(db=db, item=item, user_id=user_id)
    except TypeError as e:
        # catch the TypeError, return 406 Not Acceptable with exception details
        raise HTTPException(status_code=406, detail=str(e))

# GET /items/
# return the registered items with their respective owners attached
@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items