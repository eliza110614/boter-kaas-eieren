import random
from bke import EvaluationAgent, start, can_win, MLAgent, is_winner, opponent, train, save, load, validate, RandomAgent, plot_validation, train_and_plot

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

    random.seed(1)
 
    my_agent = MyAgent()
    random_agent = RandomAgent()
 
    train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=50,
    trainings=100,
    validations=1000)

    my_agent = MyAgent(alpha=0.8, epsilon=0.2)

  else:
    print("Invalid option")
  
  print()
  menu()
  option = int(input("Kies je spel: "))

print("Bedankt voor het spelen van Boter, Kaas & Eieren!")

# Machine learning-agents kun je configureren door de zogenaamde hyperparameters aan te passen
#alpha
#Dit is de leerfactor van de agent. Deze bepaalt hoe snel de agent nieuwe kennis adopteert. Hoe hoger dit getal, hoe sneller de agent geneigd zal zijn om oude kennis te vervangen door nieuwe kennis.
#epsilon
#Dit is de verkenningsfactor van de agent. Deze bepaalt hoe vaak de agent nieuwe dingen probeert. Hoe hoger dit getal, hoe vaker de agent een willekeurige actie probeert in plaats van de best bekende zet.

#Beide hyperparameters zijn floating point-getallen tussen de 0 en de 1. De agent staat standaard op alpha=1.0 en epsilon=0.1.

my_agent = MyAgent(alpha=0.8, epsilon=0.2)