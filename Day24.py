import random
sides = int(input("how many sides do you want? "))
leave_game = "no"
def rollDice(sides):
    print("you rolled", random.randint(1,sides))
while leave_game == "no":
    rollDice(sides)
    leave_game = input("do you want to leave the game? ")
    
        