from typing import Annotated

from fastapi import APIRouter, Query

from ..models.game import BaseGame
from ..models.player import GamePlayer

router = APIRouter(
  prefix='/game'
)

@router.post('/create')
def createGame(gameData: BaseGame):
  pass

@router.post('/join/{gameId}')
def joinGame(gameId: Annotated[str, Query(max_length=6)], playerData: GamePlayer):
  pass