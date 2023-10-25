n = int(input())
l = int(input())

graph = {i + 1: [] for i in range(n)}

for _ in range(l):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs_recursive(node, infected):
    infected.append(node)

    for adj in graph[node]:
        if adj not in infected:
            dfs_recursive(adj, infected)

    return infected

print(len(dfs_recursive(1,[])) - 1)