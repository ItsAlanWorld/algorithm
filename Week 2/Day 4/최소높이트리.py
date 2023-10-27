import collections

n = 4
edges = [[1,0],[1,2],[1,3]]
graph = collections.defaultdict(list)

for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)

leaves = []
for i in range(n + 1):
    if len(graph[i]) == 1:
        leaves.append(i)

while n > 2:
    n -= len(leaves)
    new_leaves = []
    for leaf in leaves:
        neighbor = graph[leaf].pop()
        graph[neighbor].remove(leaf)

        if len(graph[neighbor]) == 1:
            new_leaves.append(neighbor)

    leaves = new_leaves
print(leaves)