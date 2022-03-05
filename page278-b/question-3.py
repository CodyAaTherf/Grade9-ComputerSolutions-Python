# For neg_num I am not sure about what is the most efficient way.

num = int(input("Enter the number: "))

if (num <= 0):
    pos_num = abs(num)
    print(pos_num)
if (num >= 0):
    neg_num = num - num * 2
    print(neg_num)