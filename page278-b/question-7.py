# Create a Python list of 6 numbers. Replace the 2nd , 4th and 6th numbers with the cube of the numbers to its immediate left.

list1 = [2 , 3 , 5 , 7 , 11 , 13]

print(list1)

list1[1] = list1[0] ** 3
list1[3] = list1[2] ** 3
list1[5] = list1[4] ** 3

print(list1)