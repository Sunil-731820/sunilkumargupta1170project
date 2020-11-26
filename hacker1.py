import math
first_number = int(input("enter the first number"))
second_number = int(input("enter the second number"))
if (first_number >= 1 and first_number <=math.pow(10,10)) and (second_number >= 1 and second_number <=math.pow(10,10)):
    sum = first_number + second_number
    print(sum)
    diff = first_number - second_number
    print(diff)
    product = first_number*second_number
    print(product)
