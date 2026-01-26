from contextlib import asynccontextmanager
from fastapi import FastAPI

from .dependencies import db
from .routers import game

@asynccontextmanager
async def lifespan(app: FastAPI):
  # Startup stuff here
  db.create_db_and_tables()
  yield
  # Shutdown stuff here

app = FastAPI(lifespan=lifespan)

# Import routers
app.include_router(router=game.router)