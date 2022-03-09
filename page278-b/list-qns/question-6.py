# Create a Python List containing 4 integers. Replace the 3rd and the 4th item in the list with the product of the last 2 items and print the list on the screen.

list1 = [2 , 3 , 5 , 7]

print(list1)

list1[2] = list1[2] * list1[3]
list1[3] = list1[2] * list1[3]
print(f"After multiplying last two digits: {list1}")

# Not sure what the question meant but here's a solution which works