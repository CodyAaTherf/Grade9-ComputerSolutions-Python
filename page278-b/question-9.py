# Take a number as input from the user. Store the first three positive multiples of the number in a list. Show the list on the screen.

num = int(input("Enter a number: "))

if (num >= 0):
    list1 = [num , num*2 , num*3]
    print(f"Your list is: {list1}")
elif(num < 0):
    print("Enter a positive number")
else:
    print("Invalid input")