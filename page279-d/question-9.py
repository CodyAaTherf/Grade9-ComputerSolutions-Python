# Create a Python list containing elements 5 , 6 , 7 , 'hello' , 'world' and print the number of elemens in the list , dekete elements 6 ,7 , 'hello' from the list and print the number of elements again.
"""
Output:
5
2
"""

list = [5, 6, 7, 'hello', 'world']
print(len(list))
del list[3]
del list[3]
print(len(list))