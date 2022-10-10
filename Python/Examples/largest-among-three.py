# find the largest number among the three input numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 > num2) and (num1 > num3):
    print("{} is greater than {} and {}".format(num1, num2, num3))
elif (num2 > num1) and (num2 > num3):
    print("{} is greater than {} and {}".format(num2, num1, num3))
else:
    print("{} is greater than {} and {}".format(num3, num1, num2))