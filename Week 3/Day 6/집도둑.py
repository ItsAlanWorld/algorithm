def rob(nums):

    if len(nums) <= 1:
        return max(nums)

    d = [0] * len(nums)

    d[0] = nums[0]
    d[1] = nums[1]

    for i in range(2, len(nums)):
        d[i] = max(nums[i]+max(d[:i-1], default=0), d[i-1])

    return d

nums = [1,2,3,1]
print(max(rob(nums)))
