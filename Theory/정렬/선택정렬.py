def selection_sort(data):
    for stand in range(len(data) - 1):
        min = stand
        for index in range(stand+1, len(data)):
            if data[min] > data[index]:
                min = index
        data[min], data[stand] = data[stand], data[min]

    return data


import random
data_list = random.sample(range(100),30)
print(data_list)
print(selection_sort(data_list))