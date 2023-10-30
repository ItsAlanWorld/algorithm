import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")


def input():
    return sys.stdin.readline().strip()

coords = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    coords.append([x,y])

coords.sort()

for x, y in coords:
    print(x, y)