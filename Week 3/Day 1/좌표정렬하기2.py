import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input2.txt", "r")


def input():
    return sys.stdin.readline().strip()

coords = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    coords.append([x,y])

def quicksort(lst, start, end):
    def partition(part, ps, pe):
        pivot = part[pe][1]
        i = ps - 1
        for j in range(ps,pe):
            if part[j][1] == pivot:
                if part[j][0] <= part[pe][0]:
                    i += 1
                    part[i], part[j] = part[j], part[i]
            if part[j][1] < pivot:
                i += 1
                part[i], part[j] = part[j], part[i]

        part[i + 1], part[pe] = part[pe], part[i+1]
        return i + 1

    if start >= end:
        return None

    p = partition(lst, start, end)
    quicksort(lst, start, p - 1)
    quicksort(lst, p+1, end)
    return lst

result = quicksort(coords, 0, len(coords) -1 )
for x, y in result:
    print(x, y)