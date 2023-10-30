import sys

sys.stdin = open("input3.txt", "r")


def input():
    return sys.stdin.readline().strip()

data = set()

for _ in range(int(input())):
    data.add(input())

words = list(data)

words.sort(key=lambda x : (len(x), x))

for word in words:
    print(word)






