import collections

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    priorities = list(map(int, input().split()))
    q = collections.deque()
    result = []
    for i in range(n):
        q.append([i, priorities[i]])

    if len(q) == 1:
        pass

    while q:
        if any(q[0][1] < q[x][1] for x in range(1, len(q))):
            q.append(q.popleft())
        else:
            result.append(q.popleft())

    for i in range(len(result)):
        if result[i][0] == m:
            print(i + 1)


