print("Math Game")
fact_num = int(input("what multiples do you want? "))
counter = 0
for i in range(1, 10):
    correct_answer = i*fact_num
    print(i, "x", fact_num)
    your_answer = int(input("Answer: "))
    if your_answer == correct_answer:
        print("you got it right")
        counter += 1
    else:
        print("you got it wrong")
if counter == 10:
    print("wow brilliant! Perfect Score")
else:
    print("you got", counter, "out of 10 correct")