import collections
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
def input():
	return sys.stdin.readline().strip()

n = [ x for x in range(int(input())) ]
m = [int(x) for x in input().split(' ')]
k = int(input())

q = collections.deque()

q.append(n[k])
lst = []
while q:
    k = q.popleft()
    lst.append(k)
    for i in range(len(n)):
        if m[i] == k:
            q.append(i)

lst.sort(reverse=True)
for i in lst:
    m.pop(i)

counter = collections.Counter(m)
result = -1
for element, count in counter.items():
    if count >= 1:
        result += 1

if result == -1 :
    print(0)
else:
    print(result)
print(int(len(m) / 2 + len(m) % 2))