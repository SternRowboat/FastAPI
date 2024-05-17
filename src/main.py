from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


from api.v3.routes import users, items
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.main.router)
app.include_router(items.main.router)
# ----------------------------------------
from src.config.database import engine

from src.routes.users import main, models
from src.routes.auth import main, models

users.models.Base.metadata.create_all(bind=engine)
auth.models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
