import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
def input():
    return sys.stdin.readline().strip()

N = int(input())
graph = {}

for i in range(N):
    graph[i] = [int(x) for x in input()]


result = 0
result2 = []

def linked(x, y, count):
    if x < 0 or y < 0 or x >= N or y >= N:
        return count

    if graph[x][y] == 1:
        graph[x][y] = 0

        count = linked(x, y - 1, count + 1)
        count = linked(x, y + 1, count)
        count = linked(x - 1, y, count)
        count = linked(x + 1, y, count)

        return count
    return count

for i in range(N):
    for j in range(N):
        count = linked(i,j,0)
        if count > 0:
            result += 1
            result2.append(count)

print(result)
result2.sort()
for i in result2:
    print(i)







