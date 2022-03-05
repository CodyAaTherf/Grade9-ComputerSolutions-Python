# Take 3 numbrs as input from the user. Store these numbers in a list. Display their product on the screen.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

list1 = [a , b , c]
print(f"Your list is: {list1}")

list1[0] = a**2
list1[1] = b**2
list1[2] = c**2

print(f"Your List after multiplying the numbers: {list1}")