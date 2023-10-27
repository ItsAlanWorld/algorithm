import heapq

nums = [3,4,5,2]

def max_product(nums):
    max1 = max(nums)
    nums.remove(max1)
    max2 = max(nums)
    return (max1 - 1) * (max2 - 1)



print(max_product(nums))