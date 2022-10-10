# Given an integer n, return true if it is a power of three. Otherwise, return false.

def isPowerOfThree(n):
    if(n<=0):
        return False
    elif n==1:
        return True
    elif (n%3==0):
        return isPowerOfThree(n/3)
    else:
        return False
            
n = 27
print(isPowerOfThree(n))