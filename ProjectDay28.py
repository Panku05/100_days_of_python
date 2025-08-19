import random, os, time

def rollDice(number):
    answer = random.randint(1, number)
    return answer

def rollDice_6_and_12_():
    rollDice_6_sided_dice = rollDice(6)
    rollDice_12_sided_dice = rollDice(12)
    health = (rollDice_6_sided_dice * rollDice_12_sided_dice / 2) + 10
    return health

def rollDice_4_and_8_():
    rollDice_4_sided_dice = rollDice(4)
    rollDice_8_sided_dice = rollDice(8)
    strength = (rollDice_4_sided_dice * rollDice_8_sided_dice / 2) + 10
    return strength

    


print("Battle Time")
print()
p1name = input("name of the character > \n")
p1type = input("character type (human, imp, wizard, elf,): \n")
print()
print(p1name)
p1Health = rollDice_6_and_12_()
p1Strength = rollDice_4_and_8_()
print("Health:", p1Health)
print("Strength:", p1Strength)
print()
print("Who are they battling? ")
print()

p2name = input("name of the character > \n")
p2type = input("character type (human, imp, wizard, elf,): \n")
print()
print(p2name)
p2Health = rollDice_6_and_12_()
p2Strength = rollDice_4_and_8_()
print("Health:", p2Health)
print("Strength:", p2Strength)
print()
    
round = 1
winner = None
    
while True:
    time.sleep(1)
    os.system("cls")
    print("Battle Time")
    print()
    print("Battle Begins!")
    
    p1Dice = rollDice(6)
    p2Dice = rollDice(6)
    
    difference = abs(p1Strength - p2Strength) + 1
    
    if p1Dice > p2Dice:
        p2Health -= difference
        if round == 1:
            print(p1name, "wins the first blow")
        else:
            print(p1name, "wins round", round)
    elif p2Dice > p1Dice:
        p1Health -= difference
        if round == 1:
            print(p2name, "wins the first blow")
        else:
            print(p2name, "wins round", round)
    else:
        print("Their swords clashed! and they draw round", round)
        
    print()
    print(p1name)
    print("Health:", p1Health)
    print()
    print(p2name)
    print("Health:", p2Health)
    print()
    
    if p1Health <= 0:
        print(p1name, "has died")
        winner = p2name
        break
    elif p2Health <= 0:
        print(p2name, "has died")
        winner = p1name
        break

    else:
        print("and they are both standing for the round")
        round += 1
    
time.sleep(1)
os.system("cls")
print("Battle Time")
print()
print(winner,"has won in", round, "rounds")
    
    
    
    