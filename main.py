import random
from bke import EvaluationAgent, start, can_win, MLAgent, is_winner, opponent, RandomAgent, train_and_plot, train, save

#start menu om te kiezen welk spel je wilt spelen
def menu():
  print("[1] - Tegen een ander persoon spelen")
  print("[2] - Tegen een domme tegenstander spelen")
  print("[3] - Tegen een slimme tegenstander spelen")
  print("[4] - De tegenstander trainen")
  print("[5] - Validatie grafiek plotten")
  print("[0] - Stop met spelen")
  print()

#begin spel
print("Welkom bij Boter, Kaas & Eieren!")
print("Kies hieronder welk soort spel je wilt spelen:")
print()

menu()
option = int(input("Kies je spel: "))

#spelopties in 1 grote while-functie
while option != 0:
  #multiplayer
  if option == 1:
    start()
    
  #domme speler  
  elif option == 2:
    class MyRandomAgent(EvaluationAgent):
      def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1, 500)

    my_random_agent = MyRandomAgent()
    start(player_o=my_random_agent)
    
  #slimme speler  
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
    
 
    my_agent = MyAgent()
 
    train(my_agent, 3000)
 
    save(my_agent, 'MyAgent_3000')
    
  #agent trainen
  elif option == 5:
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
    
    #hyperparameters: met het aanpassen van een hyperparameter kan je machine learning-agent configureren. er zijn 2 verschillende hyperparameters: 
    #alpha: de leerfactor van de agent. bepaalt de snelheid waarmee de agent nieuwe kennis adopteert. hoe hoger het getal, hoe hoger de snelheid waarmee de agent zijn oude kennis zal vervangen met nieuwe kennis
    #epsilon: de verkenningsfactor van de agent. bepaalt hoe vaak de agent nieuwe dingen zal proberen. hoe hoger het getal, hoe vaker de agent een random actie probeert ipv iets bekends.
    #een hyperparameter is een floating point-getal tussen de 0 en 1. standaard staat de 9agent op alpha-1.0 en epsilon=0.1.
    
    my_agent = MyAgent(alpha=0.8, epsilon=0.2)

  #als er een invalid teken wordt ingevoerd
  else:
    print("Invalid option")
  
  print()
  menu()
  option = int(input("Kies je spel: "))

#einde van het spel
print("Bedankt voor het spelen van Boter, Kaas & Eieren!")