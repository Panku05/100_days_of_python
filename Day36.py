listName = []

def nameList():
    for names in listName:
        print(names)
    print()
    
while True:
    
    firstName = input("First Name: ").strip().capitalize()
    lastName = input("Surname: ").strip().capitalize()
    names = (f"{firstName} {lastName}")
    if names in listName:
        print("error! this name exists already")
    else:
        listName.append(names)
    nameList()