from typing import Annotated

from fastapi import APIRouter, Form

from ..models.game import BaseGame
from ..models.player import GamePlayer
from ..dependencies import db

router = APIRouter(
  prefix='/game'
)

@router.post('/create')
def createGame(gameData: Annotated[BaseGame, Form()], db_session: db.SessionDep):
  pass

@router.post('/join')
def joinGame(playerData: Annotated[GamePlayer, Form()], db_session: db.SessionDep):
  pass