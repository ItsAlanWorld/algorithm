import sys

sys.stdin = open("운동.txt", "r")

def input():
    return sys.stdin.readline().strip()


INF = int(1e9)
V, E = map(int,input().split())

graph = [[INF] * (V + 1) for _ in range(V + 1)]


for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a][b] = c

for i in range(1, V + 1):
    graph[i][i] = 0
result = INF
for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            if a != b:
                result = min(result, graph[a][b] + graph[b][a])

if result >= INF:
    print(-1)
else:
    print(result)

