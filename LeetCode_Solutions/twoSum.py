# 1. Two Sum

def twosum(arr, target):
  dict = {}
  for idx, val in enumerate(arr):
    if target - val in dict:
      return [dict[target - val], idx]
    else:
      dict[val] = idx

arr = [1,2,3,4,5]
target = 7
print(twosum(arr, target))
