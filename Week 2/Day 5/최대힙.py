import heapq
import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input2.txt", "r")


def input():
    return sys.stdin.readline().strip()


N = int(input())
lst = []
heapq.heapify(lst)
for _ in range(N):
    x = -int(input())
    if x == 0:
        if len(lst) > 0:
            print(-heapq.heappop(lst))
        else:
            print(0)
    else:
        heapq.heappush(lst, x)


