import heapq
import sys

INF = int(1e9)

sys.stdin = open("전보.txt", "r")

input = sys.stdin.readline

n, m, c = map(int, input().split())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))

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


result = dijkstra(c)
result.pop(c)
result = [x for x in result if x != INF]

print(len(result), max(result))

