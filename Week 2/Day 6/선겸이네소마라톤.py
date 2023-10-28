import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")
def input():
	return sys.stdin.readline().strip()

T = int(input())

lst = []
for _ in range(T):
	h, m, s = map(int, input().split())
	lst.append([h,m,s])

results = sorted(lst, key=lambda x: (x[0], x[1], x[2]))

for result in results:
	print(' '.join(map(str, result)))