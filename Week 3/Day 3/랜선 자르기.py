import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")


def input():
    return sys.stdin.readline().strip()


T, N = map(int,input().split())

nums = []
for _ in range(T):
    nums.append(int(input()))

start = 0
end = sum(nums) // N

while start <= end :
    total = 0
    mid = (start + end) // 2
    if start + end == 1:
        mid = 1
    for num in nums:
        total += num // mid

    if total < N:
        end = mid - 1
    else:
        start = mid + 1

print(end)