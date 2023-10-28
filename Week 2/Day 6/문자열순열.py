import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input2.txt", "r")


def input():
    return sys.stdin.readline().strip()

# def dfs(path):
#     if len(path) == len(s):
#         result.append(path)
#         return
#
#     for char in s:
#         if char not in path:
#             dfs(path + char)
#
# def get_permutations(s):
#     result = []  # result 변수를 함수 내에서 정의 및 초기화
#     dfs("")
#     return result

T = int(input())

for i in range(T):
    print("Case # " + str(i + 1) + ":")
    s = input()

    perms = [''.join(p) for p in permutations(s)]

    for perm in perms:
        print(perm)