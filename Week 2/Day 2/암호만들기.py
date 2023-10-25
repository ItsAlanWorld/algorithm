import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input2.txt", "r")


def input():
    return sys.stdin.readline().strip()


L, C = map(int, input().split())
alphabet = input().replace(" ", "")

vowels = ['a', 'e', 'i', 'o', 'u']

result = []

def combine(index,path):
    if len(path) > L:
        return

    if len(path) == L:
        is_vowel = [char in vowels for char in path].count(True)

        if is_vowel >= 1 and L - is_vowel >= 2:
            path.sort()
            path_tostr = ''.join(path)
            result.append(path_tostr)

    for i in range(index,C):
        combine(i+1, path + [alphabet[i]])
    result.sort()
    return result

results = combine(0,[])

for result in results:
    print(result)