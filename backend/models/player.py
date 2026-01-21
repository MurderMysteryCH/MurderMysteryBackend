from sqlmodel import SQLModel, Field
import uuid

class BasePlayer(SQLModel):
  name: str = Field(max_length=20)

class GamePlayer(BasePlayer):
  game_id: str = Field(foreign_key="game.id")

class Player(BasePlayer):
  id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
  in_game: bool = Field(default=False)