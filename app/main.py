from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


@app.get("/users/", response_model=list[schemas.User])
def read_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[type[models.User]]:
    return crud.get_users(db, skip=skip, limit=limit)


@app.get("/items/", response_model=list[schemas.Item])
def read_all_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[type[models.Item]]:
    return crud.get_items(db, skip=skip, limit=limit)


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)) -> models.User:
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)) -> models.User:
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.put("/users/{ID}", response_model=list[schemas.Item])
def update_user(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[type[models.Item]]:
    return crud.get_items(db, skip=skip, limit=limit)


@app.post("/users/{ID}/items", response_model=list[schemas.Item])
def create_user_item(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[type[models.Item]]:
    return crud.get_items(db, skip=skip, limit=limit)


@app.get("/users/{ID}/items", response_model=list[schemas.Item])
def get_user_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[type[models.Item]]:
    return crud.get_items(db, skip=skip, limit=limit)


@app.delete("/user/{ID}", response_model=list[schemas.Item])
def delete_user(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[type[models.Item]]:
    return crud.get_items(db, skip=skip, limit=limit)
