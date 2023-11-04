def max_subarray_sum(nums):
    max_sum = float('-inf')  # 최대 부분 배열 합 초기화
    current_sum = 0  # 현재까지의 부분 배열 합 초기화

    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)

        if current_sum < 0:
            current_sum = 0  # 음수인 경우 0으로 초기화

    return max_sum


# 예시 배열
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(nums)
print(result)  # 최대 부분 배열 합 출력