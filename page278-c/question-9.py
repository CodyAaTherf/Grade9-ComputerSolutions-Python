# Write a progra, to read two numbers and print their quotient and remainder

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

quotient = num1 / num2
remainder = num1 % num2

print(f"{num1} / {num2} = {quotient}")
print(f"{num1} % {num2} = {remainder}")
