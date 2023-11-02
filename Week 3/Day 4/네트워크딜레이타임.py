import heapq
import sys

input = sys.stdin.readline

flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
n = 4
src = 0
dst = 3
k = 1
cnt = 0

INF = int(1e9)
graph = [[] for i in range(n)]
distance = [INF] * (n)


for a, b, c in flights:
    graph[a].append((b, c))

def dijkstra(start, cnt):
    q = []
    heapq.heappush(q, (0, start, k))
    distance[start] = 0

    while q:
        dist, now, cnt = heapq.heappop(q)
        if distance[now] < dist:
            continue

        if cnt >= 0:
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0], cnt - 1))


    return distance[dst]

result = dijkstra(src, cnt)

print(result)




