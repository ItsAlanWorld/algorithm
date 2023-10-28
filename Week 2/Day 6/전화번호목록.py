import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input3.txt", "r")


def input():
    return sys.stdin.readline().strip()


T = int(input())

for _ in range(T):
    n = int(input())
    nums = []
    flag = 0
    for _ in range(n):
        nums.append(input())

    nums.sort()

    for i in range(1, n):
        if nums[i].startswith(nums[i - 1]):
            flag = 1
            break

    if flag == 1:
        print("NO")
    else:
        print("YES")