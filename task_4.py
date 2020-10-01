# Task 4

# Rock Paper Scissors

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game.

# Remember the rules:
#
# - Rock beats scissors
# - Scissors beats paper
# - Paper beats rock

# Function for two-player Rock-Paper-Scissors game
def rockPaperScissors(p1, p2):

  if((p1 == 'R' and p2 =='S')  # Chances of Player 1 winning
     or (p1 == 'S' and p2 =='P')
     or (p1 == 'P' and p2 =='R')):
    print("Congratulations, The Winner is Player 1")
    print("------------------------------------------")
    print()

  elif((p1 == 'S' and p2 =='R')  # Chances of Player 2 winning
     or (p1 == 'P' and p2 =='S')
     or (p1 == 'R' and p2 =='P')):
    print("Congratulations, The Winner is Player 2")
    print("------------------------------------------")
    print()
  

  print("Do you want to start a new Game ? (Y/N) ")
  print("------------------------------------------")
  print()

  ans = input()

  if(ans == 'Y'):
    newGame()
  elif(ans == 'N'):
    print("Thank You for playing the Game !! ")
    print("------------------------------------------")
    print()

  
def newGame():
  print("------------------------------------------")
  print()
  print("Welcome To The Rock Paper Scissors Game")
  print("------------------------------------------")
  print()
  print("R - indicates Rock")
  print("P - indicates Paper")
  print("S - indicates Scissors")
  print("------------------------------------------")
  print()
  print("Enter the choice for Player1 - ")
  p1 = input()
  print("Enter the choice for Player2 - ")
  p2 = input()
  print("------------------------------------------")
  print()
  rockPaperScissors(p1, p2)

# Driver Program
newGame() 
