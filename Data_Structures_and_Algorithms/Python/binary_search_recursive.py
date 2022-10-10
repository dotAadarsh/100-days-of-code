def binary_search(list_num, to_search, low, high):
    
    if low <= high:
        mid = (low + high) // 2

        if list_num[mid] == to_search:
            return mid
        
        elif list_num[mid] > to_search:
            return binary_search(list_num, to_search, low, mid-1)
        
        else:
            return binary_search(list_num, to_search, mid+1, high)

list_container = [16 , 18 , 20 , 50 , 60 , 81 , 84 , 89]
low = 0
high = len(list_container) - 1

print(binary_search(list_container , 81, low, high))
print(binary_search(list_container , 18, low, high))
print(binary_search(list_container, 10, low, high))