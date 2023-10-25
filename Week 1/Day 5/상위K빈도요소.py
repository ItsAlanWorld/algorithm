def topKFrequent(nums, k: int):
    result = {}
    for i in nums:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1
    return sorted(result, key=result.get, reverse=True)[:k]




nums = [3,2,2,1,1,1]
print(topKFrequent(nums, 2))