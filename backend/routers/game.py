from fastapi import APIRouter

from ..models.game import BaseGame
from ..models.player import GamePlayer

router = APIRouter(
  prefix='game'
)

@router.post('/create')
def createGame(gameData: BaseGame):
  pass

@router.post('/join')
def joinGame(playerData: GamePlayer):
  pass