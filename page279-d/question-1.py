# # Create a python list containing elements 1 , 2 , 3 , 4 , 5 , 6 in this order and change it to a list containing 1 , 2 , 3 , 3 , 2 , 1
# # Output [1 , 2 , 3 , 3 , 2 , 1]

list1 = [1 , 2 , 3 , 4 , 5 , 6]
print(f"You current list is {list1}")

list1[3] = 3
list1[4] = 2
list1[5] = 1

print(f"Your new list is {list1}")
