# display all the prime numbers within an interval

start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

for num in range(start, end):
    if num> 1:
        for i in range(2, num):
            if num%i == 0:
                break
            
        else:
            print(num)

