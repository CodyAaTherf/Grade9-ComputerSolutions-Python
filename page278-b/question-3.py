# Take 2 numbers as input. Convert these numbers to positive numbers if they are negative and vice versa.

num = int(input("Enter the number: "))

if (num <= 0):
    pos_num = abs(num)
    print(pos_num)
if (num >= 0):
    neg_num = -1 * num
    print(neg_num)