import heapq

nums = [3,2,3,1,2,4,5,5,6]
k = 4

def findKthLargest(nums,k):
    return heapq.nlargest(k,nums)[-1]


print(findKthLargest(nums,k))