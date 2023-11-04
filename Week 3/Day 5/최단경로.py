import heapq
import sys



sys.stdin = open("최단경로.txt", "r")

input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())
INF = int(1e9)

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

results = dijkstra(start)
results.pop(0)
for result in results:
    if result >= INF:
        print("INF")
    else:
        print(result)



