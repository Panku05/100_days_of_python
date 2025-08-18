import random
def roll_dice(number):
    result = random.randint(1, number)
    return result
def roll_dice_6_and_roll_dice_8():
    roll_dice_6_sided_dice = roll_dice(6)
    roll_dice_8_sided_dice = roll_dice(8)
    health = roll_dice_6_sided_dice * roll_dice_8_sided_dice
    return health

print("Character Health's Stat")
character_name = "yes"
while character_name == "yes":
    character = input("name your warrior: ")
    health = str(roll_dice_6_and_roll_dice_8())
    print("Their health is", health, "hp")
    character_name = input("want to create another character? ")

    
    
