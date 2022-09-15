import random
from bke import EvaluationAgent, start


class MyRandomAgent(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    getal = 1
    if board[4] == my_symbol:
      getal = getal +1
    return getal


my_random_agent = MyRandomAgent()
start(player_o=my_random_agent, player_x = my_random_agent)
