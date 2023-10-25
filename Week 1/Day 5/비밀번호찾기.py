import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(n):
    site, password = map(str, input().split())
    dict[site] = password

for i in range(m):
    site = input().strip()
    print(dict[site])

