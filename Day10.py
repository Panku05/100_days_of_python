print("tip calculator")
print()
totalBill = float(input("what's the total bill?: "))
tipPercentage = float(input("what's the tip percentage?:"))
noOfPeople = int(input("how many people?: "))
answerForTip = totalBill * tipPercentage
answer2 = answerForTip + totalBill
splitBill = answer2 / noOfPeople
splitBill = round(splitBill, 2)
print("the tip percentage is", answerForTip,"dollars")
print("you each owe", splitBill, "dollars")
