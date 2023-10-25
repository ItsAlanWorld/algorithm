data = "(()())((()))"

list = [v for v in data]

def verify(list):
    count = 0
    while len(list):
        ps = list.pop(0)
        if ps == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return "NO"
    if count == 0:
        return "YES"
    return "NO"

print(verify(list))




