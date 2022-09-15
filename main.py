import random
from bke import EvaluationAgent, start


class MyRandomAgent(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
      return random.randint(1, 500)


my_random_agent = MyRandomAgent()
start(player_o=my_random_agent)
