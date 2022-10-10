# Write a function that reverses a string. The input string is given as an array of characters s. 
# You must do this by modifying the input array in-place with O(1) extra memory.

def reverse(s):
    s[:] = s[-1::-1]

s = ["h","e","l","l","o"]
reverse(s)
print(s)

# ref - https://www.askpython.com/python/examples/colon-in-python
