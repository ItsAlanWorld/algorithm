import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("금광.txt", "r")


def input():
    return sys.stdin.readline().strip()


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    index = 0
    goldmine = []
    d = []

    #금광과 dp테이블 초기화
    for i in range(n):
        goldmine.append(lst[index:index+m])
        index += m
        d.append([0] * m)
        d[i][0] = goldmine[i][0]


    for i in range(0, n):
        for j in range(1,m):

            #왼쪽 위가 존재한다면
            if i - 1 >= 0 :
                d[i][j] = goldmine[i][j] + max(d[i][j - 1], d[i - 1][j - 1])
            #왼쪽 아래가 존재한다면
            if i + 1 < n :
                d[i][j] = goldmine[i][j] + max(d[i][j - 1], d[i + 1][j - 1])

    print(max(d[-1]))
