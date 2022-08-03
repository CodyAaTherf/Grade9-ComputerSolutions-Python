# Create a Python list containing elements a , b and remove the element b , then add elements c , d in the list.
# Output: ['a', 'c', 'd']

list = ["a", "b"]
list.remove("b")
list.append("c")
list.append("d")
print(list)