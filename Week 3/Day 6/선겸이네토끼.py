def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        print(mid, end=" ")
        if mid == target:
            return mid
        elif mid > target:
            end = mid - 1
        else:
            start = mid + 1
    return

while True:
    n = int(input())
    if n == 0:
        break
    binary_search(1,50, n)
