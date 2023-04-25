def selection_sort(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[max_index] > arr[j]:
                max_index = j
        arr[max_index], arr[i] = arr[i], arr[max_index]
    return arr


disorder_arr = [6, 3, 9, 1, 7, 2, 5]
order_arr = selection_sort(disorder_arr)
print(order_arr)
