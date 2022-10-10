# Swap Without Using Temporary Variable

x = input("Enter value of x: ")
y = input("Enter value of y: ")

x, y = y, x

print("Value after swapping: x is {} and y is {}".format(x, y))