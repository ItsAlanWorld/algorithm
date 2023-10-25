from collections import deque

T = int(input())

def verify(deque):
    count = 0
    while len(deque):
        ps = deque.popleft()
        if ps == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return "NO"
    if count == 0:
        return "YES"
    return "NO"

for _ in range(T):

    data = input()
    my_deque = deque()
    for v in data:
        my_deque.append(v)
    print(verify(my_deque))



