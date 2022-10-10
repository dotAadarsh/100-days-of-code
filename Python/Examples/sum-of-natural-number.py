# Find the Sum of Natural Numbers

num = int(input("Enter the number: "))

if num < 0:
   print("Enter a positive number")
else:
    sum_num = num * (num+1) / 2
    print(sum_num)