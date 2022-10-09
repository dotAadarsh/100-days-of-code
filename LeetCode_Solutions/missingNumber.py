# 268. Missing Number

def missing_number(nums):
    sum_of_len = sum(range(len(nums)+1))
    return sum_of_len - sum(nums)
    
nums = [3,0,1]
print(missing_number(nums))