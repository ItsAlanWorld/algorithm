n = int(input())
num = 1
washed = []
dried = []

for _ in range(n):
    while True:
        try:
            c, d = map(int, input().split())
            if c == 1:
                for _ in range(d):
                    washed.append(num)
                    num += 1
            else:
                for _ in range(d):
                    dried.append(washed.pop())
        except EOFError:
            break

    while dried:
        print(dried.pop())
