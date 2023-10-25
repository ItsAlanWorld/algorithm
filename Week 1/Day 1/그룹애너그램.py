
sortedStr = []
results = []

for i in range(len(strs)):
    sortedStr.append("".join(sorted(strs[i])))

print(sortedStr)

removeDuplicates = list(set(sortedStr))
print(removeDuplicates)

results = [[] for _ in range(len(removeDuplicates))]
for i in range(len(sortedStr)):
    for j in range(len(removeDuplicates)):
        if sortedStr[i] == removeDuplicates[j]:
            results[j].append(strs[i])

print(results)

