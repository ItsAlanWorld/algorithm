nums = [2,0,2,1,1,0]


def merge(l_arr, r_arr):
    result = []
    i = j = 0
    while i < len(l_arr) and j < len(r_arr):
        if l_arr[i] < r_arr[j]:
            result.append(l_arr[i])
            i += 1
        else:
            result.append(r_arr[j])
            j += 1

    while i < len(l_arr):
        result.append(l_arr[i])
        i += 1

    while j < len(r_arr):
        result.append(r_arr[j])
        j += 1

    return result

def mergeSort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    L = lst[:mid]
    R = lst[mid:]
    return merge(mergeSort(L), mergeSort(R))

nums = mergeSort(nums)