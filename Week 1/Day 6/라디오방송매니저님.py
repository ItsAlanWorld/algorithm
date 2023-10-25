import sys
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()
def solution(n, m, k):
    callers = list(range(1, n + 1))
    index = 0
    for _ in range(k - 1):
        index = (index + m - 1) % len(callers)
        del callers[index]
        index = (index + m - 1) % len(callers)
        return callers[index]

if __name__ == "__main__":
    while True:
        n, m, k = map(int, input().split())
        if n == 0:
            break
        print(solution(n, m, k))