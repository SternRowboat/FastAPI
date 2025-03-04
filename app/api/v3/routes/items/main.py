@router.get("/")
async def get_all_users(user: User =
Depends(get_current_active_user),
                        db: Session = Depends(get_db)):
    """
    # Get a list of all users

    **Access:**
    - Admins get a list of all users.
    - Users with lower rights get a list with only the enabled users.
    """
    if user.super_admin:
        return get_users_admin(db=db)
    else:
        return get_users(db=db)


router = APIRouter(
    prefix="/items",
    tags=["Items"],
    responses={404: {"description": "Not found"}},
)

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