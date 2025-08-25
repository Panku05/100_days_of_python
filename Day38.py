# myString = "Day 38"
# for letter in myString:
#     if letter.lower() == "a":
#         print('\033[33m', end='') #yellow
#     print(letter)
#     print('\033[0m', end='') #back to default

# vowels = ["a","e","i","o","u"]

# myString = "Will my vowels now be yellow?"
# for letter in myString:
#     if letter.lower() in vowels:
#         print('\033[33m', end='') #yellow
    
#     print(letter, end="")
#     print('\033[0m', end='') #back to default

words = input("input any sentence > ")
for letter in words:
    if letter.lower() == "r":
        print("\033[31m", end="")
    elif letter.lower() == "b":
        print("\033[32m", end="")
    elif letter.lower() == "o":
        print("\033[33m", end="")
    elif letter.lower() == "a":
        print("\033[34m", end="")
    print(letter, end="")
    print("\033[0m", end="")
    
        