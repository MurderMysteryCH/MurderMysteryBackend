from sqlmodel import SQLModel, Field

from .player import BasePlayer

class BaseGame(BasePlayer):
  max_players: int = Field()

class Game(BaseGame, table=True):
  id: str = Field(primary_key=True, max_length=6)