def fibo(num):
    cache = [ 0 for i in range(num+1)]
    cache[0] = 0
    cache[1] = 1

    for i in range(2, num+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[num]

while True:
    n = int(input())
    if n == 0:
        break
    print(fibo(n+1))