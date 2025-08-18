print("100 days of code quiz")
print("how many can answer correctly")
ans1 = input("what language are we writing in? ")
if ans1 == "python":
    print("correct")
else:
    print("nope")
ans2 = int(input("which lesson number is this? "))   
if (ans2 > 12):
    print("we are not quite that far yet")
elif (ans2 == 12):
    print("that's right!")
else:
    print("we have gone past that!")
