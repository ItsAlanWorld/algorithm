import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input2.txt", "r")
def input():
	return sys.stdin.readline().strip()

n, m, k = map(int, input().split())

graph = {i + 1: [] for i in range(n)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(node):
    visited = []
    need_visit = []

    need_visit.append(node)
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(sorted(graph[node]))
    return visited


def dfs(node):
    visited = []
    need_visit = []

    need_visit.append(node)
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(sorted(graph[node], reverse=True))
    return visited

print(' '.join(map(str,dfs(k))))
print(' '.join(map(str,bfs(k))))


