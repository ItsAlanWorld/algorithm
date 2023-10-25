temperatures = [73,74,75,71,69,72,76,73]


def verify(temperatures):
    result = [0] * len(temperatures)
    for i, val in enumerate(result):
        temp = temperatures.pop(0)
        for j, val in enumerate(temperatures):
            if temp < temperatures[j]:
                result[i] = j+1
                break

    return result

print(verify(temperatures))

def abc(temperatures):
    answer = [0] * len(temperatures)
    stack = []
    for i, cur in enumerate(temperatures):
        while stack and cur > temperatures[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    return answer

print(abc(temperatures))