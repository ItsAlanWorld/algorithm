import collections

n = int(input())

q = collections.deque()

for i in range(n):
    q.append(i+1)

while len(q) != 1:
    q.popleft()
    q.append(q.popleft())

print(q.pop())
