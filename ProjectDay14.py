from getpass import getpass as input
print("ROCK, PAPER ND SCISSORS")
print("-----------------------")
print("select your move(R, P, or S) ")
player_1 = input("what's your move? ")
player_2 = input("what's your move? ")
if player_1 == "R":
  if player_2 == "R":
    print("you both picked rock, draw!")
  elif player_2 == "P":
    print("player1's rock is smothered by player2's paper!")
  elif player_2 == "S":
    print("player1 smashed player2's scissors into the dust with their rock! ")
  else:
    print("invalid move by player2")
elif player_1 == "P":
  if player_2 == "R":
    print("player2's rock is smothered by player1's paper")
  elif player_2 == "P":
    print("two bits of paper flap at each other. Disappointing draw!")
  elif player_2 == "S":
    print("player1's paper is cut to pieces by player2's scissors")
  else:
    print("invalid move by player2")
elif player_1 == "S":
  if player_2 == "R":
    print("player2 smashed player1's scissors into the dust with their rock!")
  elif player_2 == "P":
    print("player2's paper is cut to pieces by player1's scissors")
  elif player_2 == "S":
    print("ka-shing! scissors bounce off each other like a doggy sword fight draw!")
  else:
    print("invalid move by player2")
else:
  print("invalid move by player1")