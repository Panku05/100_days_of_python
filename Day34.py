# import os, time
# listOfEmail = []

# def prettyPrint():
#     os.system("cls") # start by clearing the screen
#     print("listofEmail") # print the title of my program
#     print() # print a blank line
#     for email in listOfEmail: # use for loop to access list
#         print(email)
#     time.sleep(1)

# while True:
#     print("SPAMMER Inc.")
#     menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
#     if menu == "1":
#         email = input("Email > ")
#         listOfEmail.append(email)
#     elif menu =="2":
#         email = input ("Email > ")
#         if email in listOfEmail:
#             listOfEmail.remove(email)
#     prettyPrint()  
#     time.sleep(1)
#     os.system("cls")



# import os, time # creating a numbered list
# listOfEmail = []

# def prettyPrint():
#     os.system("cls") 
#     print("listofEmail") 
#     print()
#     counter = 1 
#     for email in listOfEmail: 
#         print(f"{counter}: {email}") 
#         counter += 1 
#     time.sleep(1)
    
# def spamming(max):
#     for i in range(0, max):
#         print(f"""Email {i+1}
            
#     Dear {listOfEmail[i]}       
#     It has come to our attention that you're missing out on the amazing Replit 100 days of code.
#     We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered 
#     and also sign you up to the My Little Pony newsletter, because that's neat. 
#     We might just do that anyway.
#     Love and hugs,
#     Ian Spammington III""")
#         time.sleep(1)
#         os.system("cls")
    

# while True:
#     print("SPAMMER Inc.")
#     menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
#     if menu == "1":
#         email = input("Email > ")
#         listOfEmail.append(email)
#     elif menu =="2":
#         email = input ("Email > ")
#         if email in listOfEmail:
#             listOfEmail.remove(email)
#     elif menu == "3": 
#         prettyPrint()
#     elif menu == "4":
#         spamming(10)
#     time.sleep(1)
#     os.system("cls")
    
    
import os, time # Using the index
listOfEmail = []



def prettyPrint():
    os.system("cls") 
    print("listofEmail") 
    print()
    for index in range(len(listOfEmail)): # len counts how many items in a list
        print(f"{index}: {listOfEmail[index]}") 
    time.sleep(1)

while True:
    print("SPAMMER Inc.")
    menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
    if menu == "1":
        email = input("Email > ")
        listOfEmail.append(email)
    elif menu =="2":
        email = input ("Email > ")
        if email in listOfEmail:
            listOfEmail.remove(email)
    elif menu == "3":
        prettyPrint() 
    time.sleep(1)
    os.system("cls")