def solution(n):
    answer = [[]]
    stack1 = [x+1 for x in range(n)]
    stack2 = []
    stack3 = []

    if n % 2 == 0:
        pass
    else:
        stack3.append(stack1.pop())
        stack2.append(stack1.pop())
        stack2.append(stack3.pop())
        stack3.append(stack1.pop())
        stack1.append(stack2.pop())
        stack3.append(stack2.pop())
        stack3.append(stack1.pop())

    print(stack1, stack2, stack3)

    return answer

solution(3)



