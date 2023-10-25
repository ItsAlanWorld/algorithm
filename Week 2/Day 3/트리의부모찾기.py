import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
def input():
	return sys.stdin.readline().strip()


n = int(input())

graph = {i + 1: [] for i in range(n)}

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(graph)