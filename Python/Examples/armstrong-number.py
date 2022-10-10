# Check Armstrong number of n digits

num = int(input("Enter the number: "))
order = len(str(num))
sum = 0
temp = num

while temp != 0:
    digit = temp % 10 
    sum += digit ** order
    temp //= 10

if sum == num:
    print("Its an armstrong number")
else:
    print("Its not an armstrong number")