nums = [1,2,3]
def subsets(nums):
    result = []


    def dfs(index, subset):
        result.append(subset)
        for i in range(index, len(nums)):
            dfs(i + 1, subset + [nums[i]])

    dfs(0, [])
    return result

print(subsets(nums))

