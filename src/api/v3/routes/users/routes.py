

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


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[type[models.Item]]:
    return crud.get_items(db, skip=skip, limit=limit)
