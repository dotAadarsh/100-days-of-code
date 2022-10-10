# Python Program to find the area of triangle

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
a = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print("The area of the triange is:", a)