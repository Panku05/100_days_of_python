print("Guess the Number Game")
print()
correct_number = 400000
counter = 1
while True:
    guess_the_number = int(input("what's your guess?: "))
    if guess_the_number < 0:
        exit()
    if guess_the_number < correct_number:
        print("your guess is too low")
        counter += 1
    elif guess_the_number > correct_number:
        print("your guess is too high")
        counter += 1
    elif guess_the_number == correct_number:
        print("yay! you got it right😍")
        break
print("you got the correct number in", counter, "attempt(s)")



    

