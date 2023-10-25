dict = {
    "2" : ["a","b","c"],
    "3" : ["d","e","f"],
    "4" : ["g","h","i"],
    "5" : ["j","k","l"],
    "6" : ["m","n","o"],
    "7" : ["p","q","r","s"],
    "8" : ["t","u","v"],
    "9" : ["w","x","y","z"],
}
result = []
digits = "23"

def letterCombinations(digits):
    def dfs(index, path):
        if len(path) == len(digits):
            result.append(path)
            return

        for i in range(index, len(digits)):
            for j in dict[digits[i]]:
                dfs(i+1, path+j)

    dfs(0,"")
    return result


print(letterCombinations(digits))
