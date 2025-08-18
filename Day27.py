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

while True:
    print("Character Builder")
    name = input("name of the character > \n")
    type = input("character type (human, imp, wizard, elf,): \n")
    print(name)
    print("Health:", rollDice_6_and_12_())
    print("Strength:", rollDice_4_and_8_())
    print()
    print("May your name go down in legend...")
    print()
    exit = input("Exit? \n")
    if exit == "yes":
        break
    time.sleep(1)
    os.system("cls")
        
    
    
    
    
    
    
    