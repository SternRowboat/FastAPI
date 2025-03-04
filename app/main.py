from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.api.v3.routes.users.main import router as users_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(users_router)

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
