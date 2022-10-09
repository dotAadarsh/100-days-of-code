def binary_search(list_num, to_search):
    low = 0
    high = len(list_num) - 1

    while low <= high:
        mid = (low + high) // 2
        if list_num[mid] == to_search:
            return f"{list_num[mid]} is found at the index {mid}"
        elif list_num[mid] < to_search:
            low = mid + 1
        else:
            high = mid - 1
    return "Not found"

list_container = [16 , 18 , 20 , 50 , 60 , 81 , 84 , 89]
print(binary_search(list_container , 81))
print(binary_search(list_container , 18))
print(binary_search(list_container, 10))