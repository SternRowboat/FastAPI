from sqlalchemy.orm import Session

from app import models, schemas
from app.models import Item, User


def get_user(db: Session, user_id: int) -> models.User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> models.User:
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[type[User]]:
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100) -> list[type[Item]]:
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int) -> models.Item:
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_user_items(db: Session, user_id: int) -> models.Item:
    pass


# TODO if all these funcs are going to use a db session
#  then I can wrap them with a decorator
def delete_user(db: Session, user_id: int) -> models.User:
    pass


def update_user(db: Session, user_id: int) -> models.User:
    pass
