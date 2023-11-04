import sys

sys.stdin = open("미래도시.txt", "r")

input = sys.stdin.readline


INF = int(1e9)
n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, y = map(int, input().split())

for i in range(n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = graph[1][y] + graph[y][x]

if result >= INF:
    print(-1)
else:
    print(result)

