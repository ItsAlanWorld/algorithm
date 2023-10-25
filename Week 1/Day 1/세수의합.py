nums = [-1,0,1,2,-1,-4]
results = []
temp = []

for i in range(len(nums) - 2):
    j = i+1
    k = len(nums) -1
    while j < k :
        while j < k :
            if nums[i] + nums[j] + nums[k] == 0:
                results.append(sorted([nums[i] , nums[j] , nums[k]]))
            j += 1
        j = i + 1
        k -= 1


results = [list(tpl) for tpl in set(map(tuple, results))]

print(results)















