t1 = input()
n = [int(x) for x in input().split()]

t2 = input()
m = [int(x) for x in input().split()]

dict = {x:1 for x in n}

for i in m:
    if dict.get(i,0) == 1:
        print(1)
    else:
        print(0)
