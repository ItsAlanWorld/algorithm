import bisect

numbers = [3,24,50,79,88,150,345]
target = 200

def twoSum(numbers, target):
    for i in range(len(numbers)):
        sub_target = target - numbers[i]
        if bisect.bisect_left(numbers, sub_target) >= len(numbers):
            continue
        if numbers[bisect.bisect_left(numbers, sub_target)] in numbers:
            if bisect.bisect_left(numbers, sub_target) == i:
                continue
            elif sub_target - numbers[bisect.bisect_left(numbers, sub_target)] == 0 :
                return sorted([i+1, bisect.bisect_left(numbers, sub_target) + 1])


print(twoSum(numbers,target))
