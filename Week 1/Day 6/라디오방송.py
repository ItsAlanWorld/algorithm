def radio():
    n, m, k = map(int, input().split())

    if n==0 and m==0 and k==0 or n < k or n > 200 or m > 200 or k > 200:
        return

    list = [x+1 for x in range(n)] # [1,0,3,0,5,6,0,8,9,10]
    # [1,0,0,0,4,5,6]
    p = -1

    result = []
    for i in range(k):
        for _ in range(m):
            p+=1
            if p >= n:
                p = p - n
            while list[p] == 0:
                p+=1
            if p >= n:
                p = p - n
        result.append(list[p])
        list[p] = 0
    return result.pop()

print(radio())