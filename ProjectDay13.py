print("GRADE GENERATOR")
print()
maxScore = int(input("what's the maximum score? "))
yourScore = int(input("what did you score? "))
print()

percentageScore = round(float(yourScore / maxScore)*100, 2)
finalNumScore = round(percentageScore, 2)
if percentageScore >= 90 and percentageScore <= 100:
    print("A+")
    print("you got", percentageScore, "%")
elif percentageScore >= 80 and percentageScore <= 89:
    print("A")
    print("you got", percentageScore, "%")
elif percentageScore >= 70 and percentageScore <= 79:
    print("B")
    print("you got", percentageScore, "%")
elif percentageScore >= 60 and percentageScore <= 69:
    print("C")
    print("you got", percentageScore, "%")
elif percentageScore >= 50 and percentageScore <= 59:
    print("D")
    print("you got", percentageScore, "%")
elif percentageScore < 49:
    print("F")
    print("you got", percentageScore, "%")
else:
    print("invalid")

