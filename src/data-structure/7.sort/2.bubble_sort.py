def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


disorder_arr = [6, 3, 9, 1, 7, 2, 5]
order_arr = bubbleSort(disorder_arr)
print(order_arr)
