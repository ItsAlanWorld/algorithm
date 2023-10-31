# import bisect
#
# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# target = 20
#
# def searchMatrix(matrix, target):
#     for i in range(len(matrix)):
#         index = bisect.bisect_left(matrix[i],target)
#
#         if index < len(matrix[i]) and matrix[i][index] == target:
#             return "true"
#     return "false"
#
# print(searchMatrix(matrix, target))

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:  # 빈 행렬인 경우
        return False

    # 왼쪽 하단에서 시작
    row, col = len(matrix) - 1, 0

    while row >= 0 and col < len(matrix[0]):
        current_value = matrix[row][col]

        if current_value == target:
            return True
        elif current_value < target:
            col += 1  # 오른쪽으로 이동
        else:
            row -= 1  # 위로 이동

    return False  # target을 찾지 못한 경우

# 예시 입력과 호출
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20
result = searchMatrix(matrix, target)
print(result)