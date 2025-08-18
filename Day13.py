print("GRADE GENERATOR")
print()
maxScore = int(input("what's the maximum score? "))
yourScore = int(input("what did you score? "))
print()

percentageScore = round(float(yourScore / maxScore)*100, 2)
finalNumScore = round(percentageScore, 2)
print("you got", percentageScore, "%")
if percentageScore >= 90 and percentageScore <= 100:
    print("A+")
elif percentageScore >= 80 and percentageScore <= 89:
    print("A")
elif percentageScore >= 70 and percentageScore <= 79:
    print("B")
elif percentageScore >= 60 and percentageScore <= 69:
    print("C")
elif percentageScore >= 50 and percentageScore <= 59:
    print("D")
elif percentageScore < 49:
    print("F")
else:
    print("you did not write the test")