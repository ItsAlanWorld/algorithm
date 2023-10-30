import sys

sys.stdin = open("input4.txt", "r")


def input():
    return sys.stdin.readline().strip()

lst = []

for _ in range(int(input())):
    age_str, name = input().split()
    age = int(age_str)
    lst.append([age, name])


results = sorted(lst, key=lambda x: (x[0]))

for age, name in results:
    print(age, name)