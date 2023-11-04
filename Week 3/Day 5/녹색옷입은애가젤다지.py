import heapq
import sys

sys.stdin = open("젤다.txt", "r")

def input():
    return sys.stdin.readline().strip()


INF = int(1e9)
cycle = 0
while 1:
    cycle += 1
    N = int(input())
    if N == 0 :
        break
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    def escape(graph):
        dr = [1, 0, -1, 0]
        dc = [0, 1, 0, -1]

        dist = [[INF] * N for _ in range(N)]

        q = []
        dist[0][0] = graph[0][0]
        heapq.heappush(q, (graph[0][0], 0, 0))
        while q:
            acc, r, c = heapq.heappop(q)

            if dist[r][c] < acc:
                continue

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:
                    cost = dist[r][c] + graph[nr][nc]
                    if cost < dist[nr][nc]:
                        dist[nr][nc] = cost
                        heapq.heappush(q, (cost, nr, nc))

        return dist[N - 1][N - 1]

    print(f"Problem {cycle}: {escape(graph)}")

