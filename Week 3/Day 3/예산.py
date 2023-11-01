import sys

sys.stdin = open("input2.txt", "r")

def input():
    return sys.stdin.readline().strip()


N = int(input())
G = list(map(int, input().split()))
M = int(input())

start = 1
end = max(G)

while start <= end:
    total = 0
    mid = (start + end) // 2

    for money in G:
        if money >= mid:
            total += mid
        else:
            total += money

    if total <= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)