print("List Generator")
print()
starting_num = int(input("Type your starting number"))
end_num = int(input("List your end number"))
increment_num = int(input("increment > "))
for i in range(starting_num, end_num, increment_num):
    print(i)
    