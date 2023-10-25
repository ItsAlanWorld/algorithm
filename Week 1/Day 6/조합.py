n = 5
k = 3


def combine(n, k):
    nums = [x + 1 for x in range(n)]
    result = []

    def dfs(index, combines):
        if len(combines) == k:
            result.append(combines)
            return
        for i in range(index, len(nums)):
            dfs(i + 1, combines + [nums[i]])

    dfs(0, [])
    return result

print(combine(n, k))