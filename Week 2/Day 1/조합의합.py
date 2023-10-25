candidates = [2,3,5]
target = 8

result = []
def combinationSum(candidates, target):
    def dfs(sum, index, path):

        if sum > target:
            return
        elif sum == target:
            result.append(path)
            return

        for i in range(index, len(candidates)):
            dfs(sum + candidates[i], i, path + [candidates[i]])
    dfs(0,0,[])
    return result

print(combinationSum(candidates, target))


