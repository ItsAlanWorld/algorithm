# import bisect
import sys
#
sys.stdin = open("input.txt", "r")
#
#
def input():
    return sys.stdin.readline().rstrip()
#
#
# N = int(input())
# parts = list(map(int, input().split()))
#
# M = int(input())
# reqs = list(map(int, input().split()))
#
# parts.sort()
#
# for req in reqs:
#     if req == parts[bisect.bisect_left(parts, req)]:
#         print("yes", end=' ')
#     else:
#         print("no", end=' ')
#

# 이진탐색(내장)

#########################################################################

# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None
#
# n = int(input())
# array = list(map(int, input().split()))
# array.sort()
# m = int(input())
# x = list(map(int, input().split()))
#
# for i in x:
#     result = binary_search(array, i, 0, n - 1)
#     if result != None:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

# 이진탐색(구현)

###################################################

n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 계수정렬

#####################################################

n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')


# 집합자료형

#####################################################