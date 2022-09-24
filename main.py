import random
from bke import EvaluationAgent, start, can_win


class MyRandomAgent(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    getal = 1
    if can_win(board, opponent_symbol):
      getal = getal - 1000
    return getal


my_random_agent = MyRandomAgent()
start(player_o=my_random_agent)