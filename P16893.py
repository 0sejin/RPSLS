from RPSLS_player import RPSLS_player
import random

class P16893(RPSLS_player):
  def __init__(self):
    self._list = ["rock", "paper", "scissors", "lizard", "spock"]

  def shoot(self):
    p = random.choice(self._list)
    return p

  def update(self, result: str, competitor_shot: str):
   pass

