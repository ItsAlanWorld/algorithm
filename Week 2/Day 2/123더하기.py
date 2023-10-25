import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")


def input():
    return sys.stdin.readline().strip()


T = int(input())

for i in range(T):
    total = int(input())
    nums = [1,2,3]
    result = []
    def add(sum, path):
        if sum > total:
            return

        if sum == total:
            result.append(path)
            return

        for num in nums:
            add(sum + num, path + [num])

        return len(result)
    print(add(0,[]))








