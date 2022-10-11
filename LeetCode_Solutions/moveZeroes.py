# Given an integer array nums, move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements

def move(nums):
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(0)
    return nums
    
nums = [0,1,0,3,12]
print(move(nums))
