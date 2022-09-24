import random
from bke import EvaluationAgent, start, can_win

def menu():
  print("[1] - Tegen een ander persoon spelen")
  print("[2] - Tegen een domme tegenstander spelen")
  print("[3] - Tegen een slimme tegenstander spelen")
  print("[4] - De tegenstander trainen")

menu()
option = int(input("Kies je spel"))

class MyRandomAgent(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    getal = 1
    if can_win(board, opponent_symbol):
      getal = getal - 1000
    return getal


my_random_agent = MyRandomAgent()
start(player_o=my_random_agent)