import sys

sys.stdin = open("input3.txt", "r")

def input():
    return sys.stdin.readline().strip()


N, M = map(int, input().split())

trees = list(map(int, input().split()))

start = 1
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for tree in trees:
        if tree > mid:
            cnt += tree - mid

    if cnt >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)