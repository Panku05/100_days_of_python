# myAgenda = []

# def printList():
#     print() #this is just to add an extra space between items
#     for item in myAgenda:
#         print(item)
#     print() #this is just to add an extra space between items

# while True:
#     item = input("What's next on the Agenda?: ")
#     myAgenda.append(item)
#     printList()
    
    
# myAgenda = []

# def printList():
#     print() 
#     for item in myAgenda:
#         print(item)
#     print() 

# while True:
#     menu = input("add or remove?: ")
#     if menu == "add":
#         item = input("What's next on the Agenda?: ")
#         myAgenda.append(item)
#     elif menu == "remove":
#         item = input("What do you want to remove?: ")
#         myAgenda.remove(item)
#     printList()

    
# myAgenda = []

# def printList():
#     print() 
#     for item in myAgenda:
#         print(item)
#     print() 

# while True:
#     menu = input("Add or Remove?: ")
#     if menu == "add":
#         item = input("What's next on the Agenda?: ")
#         myAgenda.append(item)
#     elif menu == "remove":
#         item = input("What do you want to remove?: ")
#         if item in myAgenda:
#             myAgenda.remove(item)
#         else:
#             print(f"{item} was not in the list")
#     printList()

import os, time

title = "To Do List Manager"
print(f"\033[31m{title: ^50}\033[0m")

toDoList = []

def createList():
    print()
    for content in toDoList:
        print(content)
    print()    
while True:
    time.sleep(1)
    os.system("cls")
    menu = input("Add, View or Edit?: ")
    if menu == "Add":
        content = input("what do you want to add? ")
        toDoList.append(content)
    elif menu == "View":
        createList()
    elif menu == "Edit":
        content = input("which item do you want to edit? ")
        if content in toDoList:
            toDoList.remove(content)
        else:
            print(f"{content} was not in the list")
    time.sleep(1)
    os.system("cls")
    
    