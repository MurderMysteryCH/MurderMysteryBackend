from fastapi import FastAPI

from .routers import game

app = FastAPI()

# Import routers
app.include_router(router=game.router)
