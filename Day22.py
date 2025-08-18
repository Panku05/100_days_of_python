import random

print("Guess the Number Game")
print()

counter = 1
while True:
    correct_number = random.randint(250, 460)
    print(correct_number)
    guess_the_number = int(input("what's your guess?: "))
    if guess_the_number < correct_number:
        print("your guess is too low")
        counter += 1
    elif guess_the_number > correct_number:
        print("your guess is too high")
        counter += 1
    elif guess_the_number == correct_number:
        print("yay! you got it right😍")
        break
    else:
        continue
print("you got the correct random number in", counter, "attempt(s)")
