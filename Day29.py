def createColor(color, word):
    if color=="red":
        print("\033[31m", word, sep="", end="")
    elif color=="green":
        print("\033[32m", word, sep="", end="")
    elif color=="blue":
        print("\033[34m", word, sep="", end="")
    else:
        print("\033[0m", word, sep="", end="")

print("Super Subroutine")
print("Only ", end="")
createColor("red", "GOD")
createColor("reset", " Can judge me ")
createColor("green", "i don't need ")
createColor("blue", "a jury")



# for i in range(0, 100):
#     print(i, end=" ")
    
    
# print("If you put ", "\033[33m", "nothing as the ", 
# "\033[35m", "end character ", "\033[32m", "then you don't ", "\033[0m", "get odd gaps ", sep="")

    
# print("If you put")
# print("\033[33m", end="") #yellow
# print("nothing as the")
# print("\033[35m", end="") #purple
# print("end character")
# print("\033[32m", end="") #green
# print("then you don't")
# print("\033[0m", end="") #default
# print("get odd gaps")    



# import os, time
# print("\033[?25l", end="")
# for i in range(1, 101):
#     print(i)
#     time.sleep(0.2)
#     os.system("cls")
# print("\033[?25h", end="")