import os, time

title = "To Do List Manager"
print(f"\033[31m{title: ^50}\033[0m")

toDoList = []

def createList():
    os.system("cls")
    print()
    counter = 1
    for content in toDoList:
        print(f"{counter}. {content}")
        counter += 1
    print() 
    time.sleep(1)   
    
while True:
    time.sleep(1)
    os.system("cls")
    menu = input("Do you want to view, add, edit, remove or erase an item from the to do list?: ")
    if menu == "add":
        content = input("what do you want to add? ")
        if content in toDoList:
            print("this content is already in the list!")
        else:
            toDoList.append(content)
    elif menu == "view":
        createList()
    elif menu == "remove":
        content = input("which content do you want to remove? ")
        if content in toDoList:
            ask = input("are you sure you want to remove this content? ")
            if ask == "yes":
                toDoList.remove(content)
            else:
                continue
        else:
            print(f"{content} was not in the list")
    elif menu == "edit":
        content = input("which content do you want to edit? ")
        if content in toDoList:
            new_content = input("what should replace it? ")
            index = toDoList.index(content)
            toDoList[index] = new_content
    elif menu == "erase":
        toDoList.clear()
        print("your toDoList has been erased!")
        time.sleep(1)
        os.system("cls")
    