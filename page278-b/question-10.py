# Take 3 names as input from the user. Store these names in a list. Shift all the three names to a single variable and delete the list.

name1 = input("Enter first name: ")
name2 = input("Enter second name: ")
name3 = input("Enter third name: ")

list1 = [name1 , name2 , name3]
print(f"Your list is {list1}")
del list1
print("Deleted List")