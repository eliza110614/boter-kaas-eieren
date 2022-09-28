import random
from bke import EvaluationAgent, start, can_win, MLAgent, is_winner, opponent, train, save, load, validate, RandomAgent, plot_validation

def menu():
  print("[1] - Tegen een ander persoon spelen")
  print("[2] - Tegen een domme tegenstander spelen")
  print("[3] - Tegen een slimme tegenstander spelen")
  print("[4] - De tegenstander trainen")
  print("[0] - Stop met spelen")
  print()

print("Welkom bij Boter, Kaas & Eieren!")
print("Kies hieronder welk soort spel je wilt spelen:")
print()

menu()
option = int(input("Kies je spel: "))

while option != 0:
  if option == 1:
    start()
    
  elif option == 2:
    class MyRandomAgent(EvaluationAgent):
      def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1, 500)

    my_random_agent = MyRandomAgent()
    start(player_o=my_random_agent)
    
  elif option == 3:
    class MyRandomAgent(EvaluationAgent):
      def evaluate(self, board, my_symbol, opponent_symbol):
        getal = 1
        if can_win(board, opponent_symbol):
          getal = getal - 1000
        return getal

    my_random_agent = MyRandomAgent()
    start(player_o=my_random_agent)

  elif option == 4:
    class MyAgent(MLAgent):
      def evaluate(self, board):
        if is_winner(board, self.symbol):
          reward = 1
        elif is_winner(board, opponent[self.symbol]):
          reward = -1
        else:
          reward = 0
        return reward

    my_agent = load('MyAgent_3000')
    my_agent.learning = False

    validation_agent = RandomAgent()
    validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)
    plot_validation(validation_result)
    print(validation_result)

  else:
    print("Invalid option")
  
  print()
  menu()
  option = int(input("Kies je spel: "))

print("Bedankt voor het spelen van Boter, Kaas & Eieren!")