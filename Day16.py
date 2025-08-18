print("Fill in the blank lyrics")
print("Type in thv blank lyrics and see if you are as cool as me")
counter = 1
while True:
    lyrics_with_blank = input("You dont need no other ____")
    if lyrics_with_blank == "body" or lyrics_with_blank == "Body":
        print("you got it")
    else:
        print("nope try again")
        counter += 1
    if lyrics_with_blank == "body":
        break
print("thanks for playing")

print("you got the correct lyrics in", counter, "attempt(s)")
                
    
    
    
        