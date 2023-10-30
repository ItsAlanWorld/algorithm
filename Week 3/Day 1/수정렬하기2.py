import heapq
import sys

sys.stdin = open("input5.txt", "r")


def input():
    return sys.stdin.readline().strip()

nums = []
for _ in range(int(input())):
    nums.append(int(input()))

heapq.heapify(nums)

while nums:
    print(heapq.heappop(nums))
