import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("정수삼각형.txt", "r")


def input():
    return sys.stdin.readline().strip()


n = int(input())

cache = [[0] for x in range(n)]

print(cache)

for i in range(n):
    cache[i] = list(map(int,input().split()))

print(cache)


